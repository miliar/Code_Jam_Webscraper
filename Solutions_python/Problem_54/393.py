#!/usr/bin/env python
import sys, string, fractions

kases = string.atoi(raw_input())+1
for kase in range(1,kases):
	line = raw_input().split()
	n = int(line[0])
	a = []
	for i in range(0,n):	
		a.append(int(line[i+1]))
	p = []
	len = 0
	for i in range(0,n):
		for j in range(0,i):
			p.append(abs(a[i] - a[j]))
			len = len + 1
	gcd = p[0]
	for i in range(1,len):
		gcd = fractions.gcd(gcd, p[i]);

	ans = gcd - a[0] % gcd;
	if ans == gcd:
		ans = 0
	print "Case #" + repr(kase) + ": %d" % ans

