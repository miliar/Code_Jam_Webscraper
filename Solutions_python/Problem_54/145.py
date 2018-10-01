#!/usr/bin/python

import sys

def readints():
	tokens = sys.stdin.readline().strip().split()
	return [int(i) for i in tokens]

def gcd(a, b):
	while b != 0:
		a, b = (b, a%b)
	return a

def tc():
	input = readints()
	N = input[0]
	secs = input[1:]
	diffs = [abs(secs[i]-secs[j]) for i in xrange(N) for j in xrange(i+1, N)]
	
	gcd_val = diffs[0]
	for v in diffs[1:]:
		gcd_val = gcd(gcd_val, v)

	mod = (secs[0] % gcd_val)
	if mod > 0:
		return gcd_val - mod
	else:
		return 0

C = readints()[0]
for i in xrange(C):
	print "Case #%d: %d" % (i+1, tc())

