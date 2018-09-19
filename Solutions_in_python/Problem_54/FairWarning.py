#!/usr/bin/env python
def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        t=a%b
        a=b
        b=t
    return a
def gcds(s):
    if len(s)==1:
        return s[0]
    g=gcd(s[0],s[1])
    s=s[2:]
    if s:
        s.append(g)
        return gcds(s)
    else:
        return g
def codejam(s):
    S=[]
    for i in range(1,len(s)):
        S.append(fabs(s[i-1]-s[i]))
    g=gcds(S)
    i=0;
    flag=False
    while not flag:
        flag=True
        for item in s:
            t=(item+i)%g
            if t!=0:
                i=i+g-t
                flag=False
    return i
from sys import stdin
from math import fabs
N=int(stdin.readline())
for case in range(1,N+1):
    s=map(int,stdin.readline().split()[1:])
    i=codejam(s)
    print "Case #%d: %d" % (case,i)
