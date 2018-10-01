#!/usr/bin/env python
import sys
import numpy as np
import time
import math
def estimate(x,y,llim):
    if(y==x and x==1):
        return -1
    if(y<x*2-1):
        return 1
    lmax = int(math.log((y*1.0)/(x*1.0))/math.log(2))+1
    #print x,y,lmax
    if(((2**lmax)*x-np.sum(2**np.arange(lmax)))>y):
     #   print 'here'
        for i in xrange(lmax):
            l = lmax-i
            #print i,l
            if(((2**l)*x-np.sum(2**np.arange(l)))<y):
                return l+1
    else:
     #   print 'here'
        l = lmax+1
        while (((2**l)*x-np.sum(2**np.arange(l)))<y and l<(lmax+llim)):
            l+=1
        return l
    return -1
def judge(case, motes):
    m0 = int(case[0])
    ln = int(case[1])
    motes = np.sort(np.array(motes))
    sum = m0
    count = 0
    #print m0,motes
    for i in xrange(ln):
     #   print i,motes[i]
        if sum<=motes[i]:
            l= estimate(sum,motes[i],llim=ln-i)
      #      print 'es',l
            if l==-1:
                count+=ln-i
                break
            if l<(ln-i):
                count+=l
                sum=(2**l)*sum-np.sum(2**(np.arange(l)))
            else:
                count+=ln-i
                break
        sum+=motes[i]
    #print answer,t 
    return count


def main():
    infile = sys.argv[1]
    fin=open(infile,mode='r')
    nT = int(fin.readline().rstrip())
    for i in xrange(nT):
        string=fin.readline().rstrip()
        case=string.split()
        string=fin.readline().rstrip()
        motes=[int(x) for x in string.split()]
        result=judge(case,motes)
        print 'Case #%d: %d' % (i+1,result)
    fin.close()
    return

if __name__=='__main__':
    main()
