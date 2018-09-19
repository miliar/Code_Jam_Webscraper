
from collections import *
from copy import *
from math import *
from fractions import *

if __name__=='__main__':
    input=open('B-large.in.txt','r+')
    output=open('B-large.out.txt','w+')

    numCases = int(input.readline().strip())
    for case in range(1,numCases+1):
        [k,l,s]=input.readline().strip().split()
        k=int(k)
        l=int(l)
        s=int(s)

        keyboards = input.readline().strip()
        target = input.readline().strip()

        r = None
        for i in range(1,l):
            h=l-i
            if target[i:]==target[:h]:
                r=i
                break
        if r==None:
            r=l

        g=(s-l)//r+1

        ke = set()
        p = dict()
        #print keyboards
        for key in keyboards:
            if key not in ke:
                ke.add(key)
                p[key]=1
            else:
                p[key]+=1

        for key in p.keys():
            p[key]=float(p[key])/k

        ta = set()
        for key in target:
            ta.add(key)

        result = 0.0
        if ta.issubset(ke):
            result = 1.0
            for key in target:
                result*=p[key]
            result*=(s-l)+1
            result = g-result
        else:
            result=0.0

        
        
        output.write("Case #%d: %f\n"%(case,result))
        

    input.close()
    output.close()