#!/usr/bin/python3

from functools import reduce
from fractions import gcd as gcd

c = int(input())
for cn in range(c):
	n, *t = map(int, input().strip().split())
	m = max(t)
	r = [m - i for i in t if i != m]
	g = reduce(gcd, r)
	if m % g:
		print('Case #%d: %d' % (cn + 1, g - m%g))
	else:
		print('Case #%d: 0' % (cn + 1))
