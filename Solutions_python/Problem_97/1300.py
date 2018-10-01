#!/usr/bin/env python

import math

def n_digits(x):
	return int(math.ceil(math.log(x + 1, 10)))

def recycle(x, n):
	left = x / 10**n
	right = x % 10**n
	return right * 10**n_digits(left) + left

T = int(raw_input())
for t in range(T):
	line = raw_input().rstrip().split()
	A, B = int(line[0]), int(line[1])

	used = set()
	for k in range(A, B+1):
		for i in range(1, n_digits(k)):
			rk = recycle(k, i)
			if n_digits(k) == n_digits(rk) and k < rk and rk <= B:
				used.add((k, rk))
	print "Case #%d: %d" % (t+1, len(used))

