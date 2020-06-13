#!/usr/bin/python3
filename = 'hanoi.result'
def file_write(text):
  with open(filename,'a') as file:
     file.write(text)

def hanoi(a,b,c,num):
  if num == 1:
     file_write(str(a +' --> ' +c+ '\n'))
  else:
     hanoi(a,c,b,num-1)
     file_write(str(a +' --> ' +c + '\n'))
     hanoi(b,a,c,num-1)

num = int(input('hanoi number: '))
hanoi('x','y','z',num)
      
