#!/usr/bin/python

import sys

def calculate(line):
  inp=line.split(" ")
  a=int(inp[0])
  b=int(inp[1])
  #lenb=len(inp[1])
  #firstb=int(inp[1][0])
  
  counter=0
  for i in range(a,b):
      stri=str(i)
      found=[]
      #samelen=(lenb==len(stri))
      for s in range(1,len(stri)):
          #if samelen and int(stri[s])>firstb:
          #   continue
          shifted=int(stri[s:]+stri[0:s])
          if shifted>i and shifted<=b and not shifted in found:
             counter+=1 
             found.append(shifted)
             #print str(i)+" "+str(shifted)
  return counter

"""
def calculate2(line):
  inp=line.split(" ")
  a=int(inp[0])
  b=int(inp[1])
  digits=len(inp[1])
  shifter=[1]
  s=1
  for i in range(0,digits-1):
     s*=10
     shifter.append(s)

  counter=0
  for i in range(a,b):
      found=[]
      for s in range(1,digits):
          shifted=shifter[-(s+1)]*(i%shifter[s])+i/shifter[s]
          if shifted>i and shifted<=b and not shifted in found:
             counter+=1 
             found.append(shifted)
             #print str(i)+" "+str(shifted)
         
  return counter
"""
   
if __name__ == "__main__":
    #findMapping("samples")
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        f = open(fn)
   
    count = int(f.readline())
    for c in range(count): 
        line=f.readline()
        print "Case #%d: %s" %(c+1,calculate(line))


