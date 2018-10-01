#!/usr/bin/python

import os,sys

f = open(sys.argv[1], 'r')

def solve(a, b, k):
	c = 0
	for i in range(a):
		for j in range(b):
			if i & j < k:
				c += 1
	return c

for t in range(int(f.readline())):
	a, b, k = map(int, f.readline().strip().split(' '))
	print "Case #%d: %s" % (t+1, solve(a, b, k))
