#!/usr/bin/python

import sys, itertools

def getl():
	return sys.stdin.readline().rstrip()

def cost(s):
	closest = sorted(s)
	i = closest.index(s[-1])
	result = abs(s[-1] - closest[i-1]) + abs(s[-1] - closest[i+1]) - 2
	#print 'cost', s, result
	return result

def cost2(s, cells, result, sum=0):
	if not cells:
		result.append(sum)
		return
	c = []
	for el in cells:
		c.append(cost(s + [el]))
	m = min(c)
	for i in range(len(cells)):
		if c[i] == m:
			#print i
			cost2(s + [cells[i]], cells[:i] + cells[i+1:], result, sum + m)

n = int(getl())

for i in range(n):
	p, q = [int(k) for k in getl().split()]
	cells = [int(k) for k in getl().split()]
	s = [0, p+1]
	result = []
	cost2(s, cells, result)
	#print p, q, cells
	print('Case #{0}: {1}'.format(i+1, min(result)))
