tc = input();
for TC in xrange(tc):
	rn1 = input();
	board1 = [[int(a) for a in raw_input().split()] for i in xrange(4)]
	rn2 = input();
	board2 = [[int(a) for a in raw_input().split()] for i in xrange(4)]
	r1 = board1[rn1-1]
	r2 = board2[rn2-1]
	results = []
	for c in r1:
		if c in r2:
			results.append(c)
	if len(results) == 1:
		print 'Case #%d: %d' % (TC+1,results[0])
	elif len(results) > 1:
		print 'Case #%d: Bad magician!' % (TC+1)
	else:
		print 'Case #%d: Volunteer cheated!' % (TC+1)
