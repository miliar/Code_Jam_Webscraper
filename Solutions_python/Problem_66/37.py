#!/usr/bin/env python

#FILE_NAME_BASE = 'B-test1'
FILE_NAME_BASE = 'B-large'
NUM_PROCESSES = 4

def parse(inp):
	numRounds, = (int(x) for x in inp.readline().split())
	maxMiss = tuple(int(x) for x in inp.readline().split())
	assert len(maxMiss) == 2 ** numRounds
	matchPrices = []
	for i in xrange(numRounds):
		prices = tuple(int(x) for x in inp.readline().split())
		assert len(prices) == 2 ** (numRounds - i - 1)
		matchPrices.append(prices)
	return numRounds, maxMiss, matchPrices

infinity = 1024 * 100000

def buildTree(numRounds, maxMiss, matchPrices):
	children = [
		(None, None, infinity, miss)
		for miss in maxMiss
		]
	for prices in matchPrices:
		siblings = []
		for i, price in enumerate(prices):
			l = children[i * 2]
			r = children[i * 2 + 1]
			node = (l, r, price, min(l[3], r[3]) - 1)
			siblings.append(node)
		children = siblings
	assert len(children) == 1
	return children[0]

def minCost(trees):
	ltrees = []
	rtrees = []
	for l, r, price, miss in trees:
		ltrees.append(l)
		rtrees.append(r)
	if ltrees[0] is None:
		return [infinity if tree[3] < 0 else 0 for tree in trees]
	lmin = minCost(ltrees)
	rmin = minCost(rtrees)
	ret = []
	for i, tree in enumerate(trees):
		l, r, price, miss = tree
		cost = lmin[i] + rmin[i]
		if miss < 0:
			cost += price
			try:
				nl = lmin[i + 1]
				nr = rmin[i + 1]
			except IndexError:
				pass
			else:
				cost = min(cost, nl + nr)
		ret.append(cost)
	return ret

def solve(numRounds, maxMiss, matchPrices):
	costTrees = []
	for i in xrange(numRounds):
		adjustedMiss = [miss - i for miss in maxMiss]
		tree = buildTree(numRounds, adjustedMiss, matchPrices)
		costTrees.append(tree)
	return minCost(costTrees)[0]

if __name__ == '__main__':
	inp = open(FILE_NAME_BASE + '.in', 'r')
	numCases = int(inp.readline())
	if NUM_PROCESSES == 0:
		results = [
			solve(*parse(inp))
			for _ in range(numCases)
			]
	else:
		from multiprocessing import Pool
		pool = Pool(NUM_PROCESSES)
		results = [
			pool.apply_async(solve, parse(inp))
			for _ in range(numCases)
			]
	inp.close()
	out = open(FILE_NAME_BASE + '.out', 'w')
	for case, result in enumerate(results):
		value = result if NUM_PROCESSES == 0 else result.get()
		out.write('Case #%d: %s\n' % (case + 1, value))
		out.flush()
	out.close()
