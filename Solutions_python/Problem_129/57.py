#!/usr/bin/python

from sys import stdin, stderr
from math import sqrt

def readiline():
	return map(int, stdin.readline().strip().split() )

tests = readiline()[0]

for test_no in xrange(1,tests+1):
	n, k = readiline()
	A = B = 0
	X = []
	for i in xrange(k):
		a, b, c = readiline()
		A -= c * (b-a)*(b-a+1) / 2
		X.append( (a,0,c) )
		X.append( (b,1,c) )
	X.sort()

	stack = []
	for a, q, c in X:
		if q == 0:
			stack.append( (a,c) )
		else:
			while c > 0:
				b, d = stack.pop()
				e = min(c,d)
				c -= e
				d -= e
				B -= e * (a-b)*(a-b+1) / 2
				if d > 0:
					stack.append( (b,d) )
	
		
	print "Case #%d: %d" % (test_no,A-B)
