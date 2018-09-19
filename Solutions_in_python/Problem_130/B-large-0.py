#!python
# -*- coding: utf-8 -*-

import sys

T = int(sys.stdin.readline().strip())

for index in range(1, T + 1):
	(N, P) = [int(x) for x in sys.stdin.readline().split()]
	A = B = 2 ** N - 1
	
	num = 1
	for i in range(1, N + 1):
		val = 2 ** i
		if val > P:
			B = num - 1
			break
		num += 2 ** (N - i)
	
	num = 1
	val = 2 ** (N - 1) + 1
	for i in range(N):
		if val > P:
			A = num - 1
			break
		val += 2 ** (N - i - 2)
		num += 2 ** (i + 1)
	print "Case #%d: %d %d" % (index, A, B)
