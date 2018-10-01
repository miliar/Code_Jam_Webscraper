#!/usr/bin/python
import sys;
import string;


def findTriple(maxScore,score):
  average=score/3;
  mod=score%3;
  if(average>=maxScore-2):
    if(mod==0):
      if(average>=maxScore-1):
        if(average==maxScore-1):
           if(average>0):
              return [(average-1,average,average+1)];
           else: return [];
        else: return [(average,average,average)];
      else: return [];
    elif(mod==1):
      if(average>=maxScore-1):
        return [(average,average,average+1)];
      else: return [];
    else:
      if(average>=maxScore-1):
         return [(average,average+1,average+1)];
      else:
         return [(average,average,average+2)];
  else:
     return [];


def isSurprising(triple):
  return (max(triple)-min(triple))==2;

lines=int(sys.stdin.readline());

for i in range(0,lines):
  numbers = string.split(sys.stdin.readline()," ");
  googlers = int(numbers[0]);
  surprising = int(numbers[1]);
  maxScore = int(numbers[2]);
  assert(maxScore>=0)
  scores = numbers[3:len(numbers)];
  dancers=0;
  for score in scores:
    triple=findTriple(maxScore,int(score));
    if(len(triple)>0):
        if(isSurprising(triple[0])):
          if(surprising>0):
               surprising-=1;
               dancers+=1;
        else:
           dancers+=1;
  print("Case #"+str(i+1)+": "+str(dancers));   
    
  
