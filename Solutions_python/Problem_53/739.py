#!/usr/bin/env python

def int2bin(n, count=30):
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

def snap(n,k):
    output=int2bin(k)
    output=output[-n:]
    #print output
    
    for i in xrange(0,len(output)):
        if output[i]=='0':
            return 'OFF'
    return 'ON'

import sys
fname=sys.argv[1]

f=open(fname,'r')
numLine=int(f.readline())
for num in xrange(1,numLine+1):
    line=f.readline().strip()
    n,k=line.split()
    n=int(n)
    k=int(k)
    
    print 'Case #'+str(num)+': '+snap(n,k)#, n , k



