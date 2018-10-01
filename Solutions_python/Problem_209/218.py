from __future__ import division

import fileinput
import math

count = int(raw_input())
case = 0

while True:
	case += 1
	if count < case:
		break

	N, K = map(int, raw_input().split())
	pancakes = []
	for n in xrange(N):
		R, H = map(int, raw_input().split())
		mantleSize = 2 * math.pi * R * H
		area = math.pi * R * R
		pancakes.append((R, H, mantleSize, area))
	pancakes.sort(key=lambda p: -p[2]) # sort by mantlesize (desc)

	syrup = 0
	largestArea = 0
	for k in xrange(K - 1):
		p = pancakes[k]
		syrup += p[2]
		largestArea = max(largestArea, p[3])
	syrup += largestArea

	bestExtra = 0
	for k in xrange(K - 1, N):
		p = pancakes[k]
		extra = 0
		extra += max(0, p[3] - largestArea) # top
		extra += p[2] # mantle
		bestExtra = max(bestExtra, extra)
	syrup += bestExtra

	print "Case #%s: %s" % (case, syrup)


