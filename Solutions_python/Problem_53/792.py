#!/usr/bin/python

T = int(raw_input())

for Case in xrange(1,T+1):
	N, K = [int(i) for i in raw_input().split()]
	
	state = K % ( 1 << N)
	print "Case #%d: " % (Case),
	if state == (1 << N) - 1:
		print "ON"
	else:
		print "OFF"
	