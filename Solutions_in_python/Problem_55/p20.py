#!/usr/bin/env python
import math
import sys
import os
from os import system

fp = open('C-small-attempt1.in','r')
fout = open('c.out','w')
str = fp.readline()
T = int(str)
for i in range(T):
	l = fp.readline().split()
	R = int(l[0])
	k = int(l[1])
	N = int(l[2])
	l = fp.readline().split()
	sum = 0
	g = []
	for j in range(N):
		g.append(int(l[j]))
		sum = sum + g[j]
	print sum
	count = 0
	rm = 0
	m = 0
	tr = 0
	newm = 0
	for j in range(R):
		temp = 0
		tr = 0
		while temp+g[m] <= k and tr < N:
			temp = temp + g[m]
			rm = rm + g[m]
			print 'temp = %d'%temp
			newm = (m + 1)%N
			tr = tr + 1
			if newm != (m+1):
				count = count + 1
				rm = 0
			m = newm
	fout.write('Case #%d: %d\n'%(i+1,(count*sum)+rm))

