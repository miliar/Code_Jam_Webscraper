#!/usr/bin/python

from mpmath import *
import sys

mp.dps = 10000
f = open(sys.argv[1])
iters = int(f.readline())

for i in range(0, iters):
	n = mpf(f.readline())
	x = mpf(3) + mpf(5) ** (mpf(1) / mpf(2))
	ans = str(x**n)
	pos = ans.find(".")
	ans = long(ans[0:pos]) % 1000

	if ans < 10:
		ans = "00" + str(ans)
	elif ans < 100:
		ans = "0" + str(ans)
	else:
		ans = str(ans)

	print "Case #%d:" % (i+1), ans
