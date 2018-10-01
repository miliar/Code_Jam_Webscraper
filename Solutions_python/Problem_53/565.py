#!/usr/bin/python

import sys
cases = int(sys.stdin.readline().strip())

for c in range(1, cases+1):
	n, k = [int(x) for x in sys.stdin.readline().strip().split(' ')]
	p = 2**n
	if k % p == (-1) % p:
		state = 'ON'
	else:
		state = 'OFF'
	print 'Case #%s: %s' % (c, state)