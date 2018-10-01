#!/usr/bin/env python

import math
import sys

with open(sys.argv[1]) as f:
	f.next()
	for case, line in enumerate(f, 1):
		stalls, people = map(int, line.strip().split())
		stalls = [stalls]
		while people:
			stall = stalls[0] - 1
			maximum = int(math.ceil(stall / 2.0))
			minimum = int(math.floor(stall / 2.0))
			if maximum == minimum == 0:
				break
			stalls = [maximum, minimum] + stalls[1:]
			stalls.sort(reverse=True)
			people -= 1
		print 'Case #%s: %s %s' % (case, maximum, minimum)
