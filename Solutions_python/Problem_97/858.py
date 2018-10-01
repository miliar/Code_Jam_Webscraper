#!/usr/bin/env python

import sys

def recycled(n,m):
    p = str(n)
    q = str(m)
    for i in range(0, len(p)):
        p = rotate(p)
        if p == q:
            return True
    return False
    
def rotate(s):
    return s[-1] + s[0:-1];

T = int(sys.stdin.readline())
for t in range(0,T):
    a,b = [int(n) for n in sys.stdin.readline().split()]
    res = 0
    for n in range(a,b+1):
        for m in range(n+1,b+1):
            if recycled(n,m):
                res+=1
    print('Case #%s: %s' % (t+1,res))

