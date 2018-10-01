t=input()
for i in xrange(t):
	n, m = map(int, raw_input().split())
	paths = {'/'}
	for j in xrange(n):
		p = ''
		for d in raw_input().strip().split('/'):
			p += d + '/'
			paths.add(p)
	x = 0
	for j in xrange(m):
		p = ''
		for d in raw_input().strip().split('/'):
			p += d + '/'
			if not p in paths:
				x += 1
				paths.add(p)
	print 'Case #%d: %d' % (i+1, x)