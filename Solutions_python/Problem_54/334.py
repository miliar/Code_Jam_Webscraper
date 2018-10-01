#!/usr/bin/env python

from sys import *

def gcd(n1, n2):
   while n2 > 0:
      tmp = n1
      n1 = n2
      n2 = tmp % n2
   return n1

f = open(argv[1], 'r')
C = int(f.readline())

for c in range(C):
	line = f.readline()
	elems = sorted(map(int, line.split())[1:], reverse=True)
	diffs = []
	for n in range(len(elems)-1):
		diffs.append(elems[n]-elems[n+1])
	greatest = diffs[0]
	for n in range(len(diffs)-1):
		greatest = gcd(greatest, diffs[n+1])	
	last = elems[len(elems)-1]
	y = greatest
	while y - last < 0:
		y += greatest
	print "Case #%d: %d" % (c+1, y-last) 
