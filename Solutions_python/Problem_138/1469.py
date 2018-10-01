#!/usr/bin/env python
import math
import sys
import os
from os import system

def war(a):
	i = 0
	j = 0
	b = []
	j = 0
	c, d = 0, 0
	while i < len(a[0]) or j < len(a[1]):
		print i, j
		if i == len(a[0]):
			state = 0
		elif j == len(a[0]):
			state = 1
		elif a[0][i] < a[1][j]:
			state = 1
		else:
			state = 0
		if state == 1:
			c, d = c, d+1
			i += 1
		elif state == 0:
			j += 1
			if d == 0:
				c, d = c+1, d
			else:
				c, d = c, d-1
	return c
			
def deceitful(a):
	i, j = len(a[0])-1, len(a[1])-1
	c, d = 0, len(a[0])
	print "*", c, d
	while i >= 0 or j >= 0:
		print i, j, c, d
		if i == -1:
			state = 0
		elif j == -1:
			state = 1
		elif a[0][i] > a[1][j]:
			state = 1
		else :
			state = 0
		if state == 1:
			c, d = c+1, d
			i -= 1
		elif state == 0:
			c, d = c, d-1
			j -= 1
		print ":", c, d
		if c == d:
			break
	return c


fp = open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
str = fp.readline()
T = int(str)
for t in range(T):
	N = int(fp.readline().split()[0])
	a = [[0.0]*N, [0.0]*N]
	for i in range(2):
		tokens = fp.readline().split()
		for j, token in enumerate(tokens):
			a[i][j] = float(token)
		a[i].sort()
	print N, a[0], a[1]
	ret_war = war(a)
	b = [[],[]]
	b[1] = a[0]
	b[0] = a[1]
	ret = len(a[0]) - war(b)
	#ret = deceitful(a) 
	fout.write('Case #%d: %d %d\n'%((t+1),ret, ret_war))
