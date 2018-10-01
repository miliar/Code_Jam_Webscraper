#!/usr/bin/python
import sys

def preProcess():
   n=len(sys.argv)
   if(n<2):
      filename=raw_input("Enter the file name : ")
   else:
      filename=sys.argv[1]

   inFilename=filename+".in"
   outFilename=filename+".out"
   infile=open(inFilename)     
   outfile = open(outFilename,"w")
   C = int(infile.readline())
   return (C,infile,outfile)


(C,infile,outfile)=preProcess()
cases = 1
while(cases <= C):
    inStr  = infile.readline()
    N = int(inStr)
    
    A=[]
    B=[]
    for i in range(0,N):
       inStr=infile.readline()
       l = inStr.split()
       a = (int(l[0]))
       b = (int(l[1]))
       A.append(a)
       B.append(b)
       
    n = 0
    while(A != []):
       a=A[0]
       b=B[0]
       A=A[1:]
       B=B[1:]
       i = 0
       for a1 in A:
          b1 = B[i]
          if (a1 < a and b1 > b):
             n=n+1
          elif(a1 > a and b1<b):
             n=n+1
    
    outStr = "Case #%d: %d" %(cases,n)
    outfile.write(outStr+"\n")
    cases = cases+1
