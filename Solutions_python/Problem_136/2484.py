#!/usr/bin/env python3

import sys
from math import sqrt

to_float7 = lambda x: "{0:.7f}".format(x)

def solve(c, f, x):
	# n >= \frac{F * X - 2 * C}{C * F}
	nfarms = int((f * x - 2.0 * c) / (c * f))
	# No need to create farms, just wait.
	if nfarms <= 0:
		return to_float7(x / 2.0)
	# Time required to create nth farm
	t = sum((c / (2.0 + i * f)) for i in range(nfarms))
	# plus the time to produce cookies with the nth farm
	return to_float7(t + x / (2 + nfarms * f))

def read_input():
	return (float(x) for x in sys.stdin.readline().split())

if __name__ == '__main__':
	ncases = int(sys.stdin.readline())
	for case in range(1, ncases + 1):
		result = solve(*read_input())
		print('Case #', case, ': ', result, sep='')
