#! /usr/bin/python
from numpy import *
import sys
import math
sys.setrecursionlimit(500000)
def recurse(x0,R):
    global F,C,X
    #print 'number of purchases',X/C-2/F
    #n = int(math.ceil(X/C-2/F-1))
    #if n > 0 and X/(2+n*F) < ( C/(2+n*F) + X/(2+(n+1)*F)) :
    #    tym = (C*array([1]*(n)))/(2+F*array(range(n)))
    #    #print 'yes'
    #    return sum(tym)+X/(2+n*F)

    t0=0
    while  X/R > (C/R+X/(R+F)):
        t1=C/R-x0
        R=R+F
        t0=t0+t1
    return t0+X/R

    #if X/R > (C/R+X/(R+F)):
    #    return min(X/R,t1+recurse(0,R+F))
    #else:
    #    return X/R


#f=open('testB')
#f=open('B-small-attempt0.in')
f=open('B-large.in')
T=int(f.readline())
for t in range(1,T+1):
    [C,F,X] = [float(x) for x in f.readline().split()]
    print 'Case','#'+str(t)+':','%0.7f'%recurse(0,2)
