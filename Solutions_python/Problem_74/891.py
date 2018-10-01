#!/usr/bin/env python

import sys

T = int(sys.stdin.readline())

for t in range(T):
	# read line
	line = sys.stdin.readline().split()
	N = int(line[0])
	leftover = 0
	c_prev = ''
	pos = {'O':1, 'B':1}
	count = 0

	# process
	for n in range(N):
		c = line[2*n+1]
		p = int(line[2*n+2])

		# move
		if c == c_prev:
			diff = abs(pos[c] - p)
			leftover += diff
			count += diff
		else:
			diff = abs(pos[c] - p)
			diff -= leftover
			if diff < 0: diff = 0
			leftover = diff
			count += diff
		c_prev = c
		pos[c] = p
		#print 'move %s %s' % (count, leftover)

		# push
		leftover += 1
		count += 1
#		print 'push %s %s' % (count, leftover)
	print 'Case #%s: %s' % (t+1, count)
