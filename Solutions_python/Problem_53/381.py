#!/usr/bin/env python

t = int(raw_input())
for i in xrange(1,t+1):
	print "Case #%d:" % i,
	n,k = raw_input().split();
	if (int(k) + 1) % 2**int(n) == 0:
		print "ON"
	else:
		print "OFF"
