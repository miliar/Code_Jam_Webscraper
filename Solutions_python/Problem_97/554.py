for t in xrange(int(raw_input())):
	A, B = map(int, raw_input().split())
	L = len(str(A))
	L10 = 10**(L - 1)
	count = 0
	S = set()
	for x in xrange(A, B + 1):
		y = x
		for i in xrange(L - 1):
			y = (y / L10) + (y%L10)*10
			if y > x and y >= A and y <= B:
				S.add((x, y))
	print 'Case #%d: %d' % (t + 1, len(S))
