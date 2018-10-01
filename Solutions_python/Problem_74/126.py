#!/usr/bin/python

# A. Bot Trust

import math
import sys

f = sys.stdin
T = int(f.readline())

for lineno in range(1, T+1):
	list = f.readline().split()
	N = int(list[0])
	list = list[1:]

	O = 1
	B = 1
	Otime = 0
	Btime = 0
	time = 0


	for i in range(N):
		R = list[i*2]
		P = int(list[i*2+1])
		if R == 'O':
			dist = abs(P - O)
			O = P
			time += max(0, dist - (time - Otime)) + 1
			Otime = time
		else:
			dist = abs(P - B)
			B = P
			time += max(0, dist - (time - Btime)) + 1
			Btime = time

	print "Case #%s: %s" % (lineno, time)
