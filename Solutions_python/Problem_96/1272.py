#!/usr/bin/python

import time, sys, os
start = time.clock()
print os.path.dirname(sys.argv[0])
sys.stdout = open(os.path.dirname(sys.argv[0]) + r'\output.txt', 'w')


f = open(sys.argv[1], 'r')
T = int(f.readline())

for i in xrange(T):
	nums = map(int, f.readline().split())
	_, S, p, x = nums[0], nums[1], nums[2], nums[3:]
	
	noreq = p*3 - 2			# A total must be greater than this value
	req = max(p, p*3 - 4)	# A total must be greater than this value
	
	noreq_surprise = sum(1 for xi in x if xi >= noreq)
	req_surprise = sum(1 for xi in x if xi < noreq and xi >= req)
	
	print 'Case #%d: %d' % (i + 1, noreq_surprise + min(req_surprise, S))