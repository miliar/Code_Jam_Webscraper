#!/usr/bin/env python
from math import ceil
from sys import stdin
f=2
T=int(stdin.readline())
for case in range(1,T+1):
	C,F,X=map(float,stdin.readline().split())
	N=max(0,int(ceil(X/C-f/F-1)))
	T=sum(C/(f+n*F) for n in range(N))+X/(f+N*F)
	print 'Case #%d:'%case, T
