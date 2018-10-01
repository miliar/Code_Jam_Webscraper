import sys, heapq

sys.stdin = open("C-small-2-attempt0.in", 'r')
sys.stdout = open("out.out", 'w')


T = input()

for t in xrange(1, T+1):
	N,K = map(int, raw_input().split())
	lst = []
	heapq.heappush(lst, -N)
	for i in xrange(K-1):
		cur = -heapq.heappop(lst)
		if cur > 1: 
			heapq.heappush(lst, -(cur/2))
		if cur > 2: 
			heapq.heappush(lst, -((cur-1)/2))
	cur = -heapq.heappop(lst)
	print "Case #%d: %d %d"%(t, cur/2, (cur-1)/2)