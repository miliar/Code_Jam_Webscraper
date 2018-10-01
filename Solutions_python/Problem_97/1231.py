#!/usr/bin/python
import sys;
import string;


def shiftStr(number,n):
  length=len(number);
  return number[length-n:length]+number[0:(length-n)];

def isRecycled(a,b):
  if(len(a)!=len(b)):
    return False;
  else:
    for i in range(0,len(a)):
       if(shiftStr(a,i)==b):
          return True;
    return False;

def countRecycled(start,end):
  count=0;
  for i in range(start,end):
    for j in range(i+1,end+1):
#       print str(i)+" "+str(j);
       if(isRecycled(str(i),str(j))):
          count+=1;
  return count;


lines=int(sys.stdin.readline());


for i in range(0,lines):
    numbers = string.split(sys.stdin.readline()," ");
    start=int(numbers[0]);
    end=int(numbers[1]);
    print("Case #"+str(i+1)+": "+str(countRecycled(start,end)));
    

