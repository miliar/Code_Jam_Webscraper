#!/usr/bin/python
import sys

t = int(sys.stdin.readline())
for case in xrange(1, t+1):
	[c, f, x] = [float(x) for x in sys.stdin.readline().split()]
	
	res = sys.maxint
	time = 0.0
	acc = 2.0
	
	while(True):
		# not take
		caltime = time + x/acc
		
		if res > caltime:
			res = caltime
		else :
			break

		# take
		time = time + c/acc
		acc = acc + f

	print "Case #%d: %.7f" % (case, res)