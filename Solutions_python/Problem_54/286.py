#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def gcd(a, b):
	while a and b:
		a %= b
		if a: b %= a
	return a + b

f = open(sys.argv[1], "r")
lines = map(lambda s: s.strip(), f.readlines())
tc = 0
for line in lines[1:]:
	tc += 1
	a = sorted(map(int, line.split())[1:])
	g = a[1] - a[0]
	for i in range(1, len(a) - 1):
		g = gcd(g, a[i + 1] - a[i])
	a0 = a[0] / g
	res = 0
	if a0 * g != a[0]:
		res = (a0 + 1) * g - a[0]
	print "Case #%d: %d" % (tc, res)
