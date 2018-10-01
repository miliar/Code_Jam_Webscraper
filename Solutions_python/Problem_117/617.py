#!/usr/bin/env pypy
import sys, os
# Cases
t = int(sys.stdin.readline())

for case in xrange(t):
	h, w = map(int, sys.stdin.readline().rstrip('\n').split())
	result = 0
	hmax = [100] * h
	wmax = [100] * w
	data = list()
	result = 'YES'
	for i in xrange(h):
		data.append(sys.stdin.readline().rstrip('\n').split())
	for i in xrange(h):
		hmax[i] = max(data[i])
	for i in xrange(h):
		hmax[i] = max(data[i])
	for i in xrange(w):
		wmax[i] = max(map(lambda x: x[i], data))
	for i in xrange(h):
		for j in xrange(w):
			d = data[i][j]
			if d < hmax[i] and d < wmax[j]:
				result = 'NO'
	print "Case #%d: %s" % (case+1, result)
