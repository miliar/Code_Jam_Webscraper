
from collections import *
from copy import *
from math import *
from fractions import *

if __name__=='__main__':
    input=open('A-large.in.txt','r+')
    output=open('A-large.out.txt','w+')

    numCases = int(input.readline().strip())
    for case in range(1,numCases+1):
        [r,c,w]=input.readline().strip().split()
        r=int(r)
        c=int(c)
        w=int(w)

        k=c//w
        k=k*r

        if c//w*w!=c:
            k+=1
        k+=(w-1)
        
        if w==1:
            k=r*c
        output.write("Case #%d: %d\n"%(case,k))
        

    input.close()
    output.close()