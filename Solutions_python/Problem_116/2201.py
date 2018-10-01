d = []
d.append((0,0,1,1))
d.append((0,3,1,-1))
for i in xrange(4):
	d.append((0,i,1,0))
	d.append((i,0,0,1))
tn = input()
for loop in xrange(tn):
	print 'Case #%d:'%(loop+1),
	b = []
	for i in xrange(4):
		b.append(raw_input())
	_ = raw_input()
	xwon = False
	owon = False
	notdone = False
	for l in b:
		if '.' in l:
			notdone = True

	for x,y,dx,dy in d:
		c = 0
		for i in xrange(4):
			if b[x][y] in 'XT':
				c += 1
			x+=dx
			y+=dy
		if c == 4:
			xwon = True

	for x,y,dx,dy in d:
		c = 0
		for i in xrange(4):
			if b[x][y] in 'OT':
				c += 1
			x+=dx
			y+=dy
		if c == 4:
			owon = True
	if xwon:
		print 'X won'
	elif owon:
		print 'O won'
	elif notdone:
		print 'Game has not completed'
	else:
		print 'Draw'

