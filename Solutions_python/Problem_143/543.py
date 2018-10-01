#! /opt/local/bin/python
from numpy import *
from itertools import *
#from gmpy2 import *
#f=open('test1')
f=open('b-small-attempt0.in')
#f=open('A-large.in')
T=int(f.readline())
for tt in range(1,T+1):
    [A,B,K]=[int(i) for i in f.readline().split()]
    count = 0;
    for i in range(A):
        for j in range(B):
            if i&j<K:
                count += 1
    print 'Case','#'+str(tt)+':',count


