from heapq import heappush, heappop
from collections import defaultdict

def process(N, K):
	minrange = N
	rangeheap = [-N]
	rangedict = defaultdict(int)
	rangedict[N] = 1

	while K>=0:
		maxrange = -heappop(rangeheap)
		k = rangedict[maxrange]
		if K > k:
			newrange = (maxrange-1)/2
			if newrange not in rangedict:
				heappush(rangeheap, -newrange)
			rangedict[newrange] += k

			newrange = maxrange/2
			if newrange not in rangedict:
				heappush(rangeheap, -newrange)
			rangedict[newrange] += k

			K -= k
			del rangedict[maxrange]
		else:
			return maxrange/2, (maxrange-1)/2

	return -1, -1

def run():
	T = int(raw_input().strip())
	for caseno in range(T):
		N, K = map(int, raw_input().strip().split())
		mx, mn = process(N,K)
		print 'Case #' + str(caseno+1) + ':', mx, mn

run()

