import sys
sys.stdin = file('a.in')
sys.stdout = file('a.out','w')
N = int(raw_input())
for loop in xrange(N):
	sol = 0
	ts = []
	n, A, B, C, D, x0, y0, M = [int(x) for x in raw_input().split()]
	for i in xrange(n):
		ts.append((x0,y0))
		x0 = (A*x0+B) % M
		y0 = (C*y0+D) % M

	for i in xrange(n):
		for j in xrange(i+1, n):
			for k in xrange(j+1, n):
				a = ts[i], ts[j], ts[k]
				x=sum(t[0] for t in a)
				y=sum(t[1] for t in a)
				if x%3 == 0 and y % 3 == 0:
					sol += 1
		
	print 'Case #%d: %d' % (loop+1, sol)
