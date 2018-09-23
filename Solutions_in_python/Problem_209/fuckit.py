import math
import itertools

cases = int(raw_input())

pi = math.pi


def findTotalSurface(pancakes):
	total = 0
	for i,v in enumerate(pancakes):
		R,H,S,T = v

		if i != 0: # not the top pancake
			Rn,Hn,Sn,Tn = pancakes[i-1]
			S -= Tn
		total += S
	return total

for case in range(cases):

	N,K = [int(i) for i in raw_input().split()]

	pancakes = []

	for i in range(N):
		R, H = [int(i) for i in raw_input().split()]
		pancakes.append((R, H))

	pancakes.sort(key=lambda tup: tup[0])

	# get surface area for all pancakes
	for i,v in enumerate(pancakes):
		R, H = v
		surfaceAreaTop = (math.pi * R ** 2.00)
		surfaceAreaSide = (2.00 * math.pi * R * H)
		S = surfaceAreaTop + surfaceAreaSide
		T = surfaceAreaTop

		pancakes[i] = (R,H,S,T)

	maxArea = 0
	# Go crazy for the small dataset
	for comb in itertools.combinations(pancakes,K):
		area = findTotalSurface(comb)
		if max(area,maxArea) == area:
			maxArea = area

	print "Case #" + str(case+1) + ": %.12f" % maxArea