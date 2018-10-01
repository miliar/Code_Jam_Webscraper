#!/usr/bin/env python

class streamreader:
	def __init__(_, s): _.t = (t for t in s.read().split())
	def __div__(_, t): return (t)(_.t.next())

import sys
reader = streamreader(sys.stdin)

def solve(N, d, l, D):
	reached = [False for _ in xrange(N)]
	p = [0 for _ in xrange(N)]
	reached[0] = True
	p[0] = d[0]
	for i in xrange(N):
		if reached[i]:
			for j in xrange(i + 1, N):
				if d[j] - d[i] <= p[i]:
					q = min(d[j] - d[i], l[j])
					if q >= p[j]:
						reached[j] = True
						p[j] = q
				else:
					break
	if reached[N - 1]:
		return 'YES'
	else:
		return 'NO'


T = reader/int
for t in xrange(1, T + 1):
	N = reader/int
	d, l = [], []
	for i in xrange(N):
		d.append(reader/int)
		l.append(reader/int)
	D = reader/int
	d.append(D)
	l.append(0)
	N += 1
	answer = solve(N, d, l, D)
	print 'Case #%d: ' % t, answer

