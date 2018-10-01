#!/usr/bin/python
# -*-coding:Latin-1 -*
import os
import math
T =int(raw_input())
for i in xrange(T):
	x = map(int, raw_input())
	din = map(int, raw_input().split())
	din = sorted(din, reverse=True)
	l = din[0]
	minute = din[0]
	for k in range(1, l + 1):
		div = 0
		for j in din:
			if j <= k:
				break
			div += math.ceil(float(j) / float(k)) - 1
		if div + k < minute:
			minute = div + k

	print('Case #%d: %d' % (i + 1, minute))
