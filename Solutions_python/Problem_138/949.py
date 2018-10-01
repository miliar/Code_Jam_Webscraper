#! /usr/bin/env python
'''
Name: Sravan Bhamidipati
Date: 12th April, 2014
Purpose: 
'''

import bisect
import sys


def war(count, nblocks, kblocks):
	score = 0

	for i in xrange(count):
		naomi = nblocks.pop()

		if naomi < kblocks[0]:
			break
		elif naomi > kblocks[-1]:
			score += 1
			kblocks.pop(0)
		else:
			kblocks.pop(bisect.bisect(kblocks, naomi))

	return score


def dewar(count, nblocks, kblocks):
	score = 0

	for i in xrange(count):
		if nblocks[-1] < kblocks[0]:
			break
		elif nblocks[-1] > kblocks[-1]:
			score += 1
			nblocks.pop()
			kblocks.pop()
		else:
			nblocks.pop(0)
			kblocks.pop()

	return score


with open(sys.argv[1]) as fd:
	for line_no, line in enumerate(fd):
		rem = line_no % 3

		if line_no == 0 or rem == 1:
			count = int(line)
		elif rem == 2:
			nblocks = sorted(map(float, line.strip().split()))
		elif rem == 0:
			kblocks = sorted(map(float, line.strip().split()))
			dwscore = dewar(count, list(nblocks), list(kblocks))
			wscore = war(count, nblocks, kblocks)
			print 'Case #%d: %d %d' % ((line_no/3), dwscore, wscore)

