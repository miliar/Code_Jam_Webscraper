import sys


T = int(raw_input())

for tt in xrange(1, T + 1):
	n = int(raw_input())
	a = [int(x) - 1 for x in raw_input().split()]
	r = 0
	for i in xrange(0, len(a)):
		if i != a[i]:
			r += 1
	print "Case #%d:" % tt, r
