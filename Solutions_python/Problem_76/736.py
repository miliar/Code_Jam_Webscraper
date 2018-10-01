# Python 2.7

from itertools import combinations
import sys

def difference(a, b):
	r = list(a)
	for i in b:
		r.remove(i)
	return r

for i in xrange(0, int(sys.stdin.readline())):
	sys.stdin.readline()
	a = list(map(int, sys.stdin.readline().split(" ")))
	best = -1
	for j in xrange(1, len(a) / 2 + 1):
		for k in combinations(a, j):
			b = difference(a, k)
			sum1 =  sum2 = xsum1 = xsum2 = 0
			for x in k:
				sum1 = sum1 + x
				xsum1 = xsum1 ^ x
			for x in b:
				sum2 = sum2 + x
				xsum2 = xsum2 ^ x
			if xsum1 == xsum2:
				best = max(max(best, sum1), sum2)
	if best == -1:
		print "Case #" + str(i + 1) +": NO"
	else:
		print "Case #" + str(i + 1) + ": " + str(best) + ""
