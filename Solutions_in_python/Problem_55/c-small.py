t = int(raw_input())
for i in xrange(1, t+1):
	r, k, n = map(int, raw_input().split())
	g = map(int, raw_input().split())
	revenue = 0
	head = 0
	for j in xrange(r):
		free = k
		oldhead = head
		while g[head] <= free:
			free -= g[head]
			head += 1
			if head == n: head = 0
			if head == oldhead: break
		revenue += k - free
	print 'Case #%u: %u' % (i, revenue)