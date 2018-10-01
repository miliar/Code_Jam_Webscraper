#!/usr/bin/env python
import math
import sys
import os
from os import system

fp = open(sys.argv[1],'r')
fout = open(sys.argv[2],'w')
str = fp.readline()
T = int(str)
for i in range(T):
	l = fp.readline().split()
	N = int(l[0])
	M = int(l[1])
	dir = {}
	name = []
	dir['/'] = []
	for j in range(N):
		l = fp.readline().split('\n')[0].split('/')
		l = l[1:]
		#dir['/'].append(l[0])
		name.append('/')
		key = ''
		for k in range(len(l)):
			key = key + '/' + l[k]
			if key in name:
				k = k
				#dir[key].append(l[k+1])
			else :
				name.append(key)
				#dir[key] = []
				#dir[key].append(l[k+1])
	#print name
	count = 0
	for k in range(M):
		l = fp.readline().split('\n')[0].split('/')
		l = l[1:]
		key = ''
		oldkey = '/'
		for d in l:
			key = key + '/' + d
			if key not in name:
				#print name
				name.append(key)
				count = count + 1
				#print key
				#dir[oldkey].append(d)
				#dir[key] = []
			oldkey = key
	fout.write('Case #%d: %d\n' % (i+1, count))

