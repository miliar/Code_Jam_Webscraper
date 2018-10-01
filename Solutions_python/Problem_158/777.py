from sys import stdin

f = open('small.out','w')
T = int(stdin.next())
ga = 'GABRIEL'
ri = 'RICHARD'

for i in xrange(1,T+1):
	x,r,c = map(int,stdin.next().split())
	if x==1:
		print 'Case #%d:' %i,ga
		print>>f, 'Case #%d:' %i,ga
		continue

	if x==2:
		if r*c % 2 == 0:
			print 'Case #%d:' %i,ga
			print>>f, 'Case #%d:' %i,ga
			continue
		else:
			print 'Case #%d:' %i,ri
			print>>f, 'Case #%d:' %i,ri
			continue
	
	if x==3:
		if r*c % 3 == 0 and r*c > 3:
			print 'Case #%d:' %i,ga
			print>>f, 'Case #%d:' %i,ga
			continue
		else:
			print 'Case #%d:' %i,ri
			print>>f, 'Case #%d:' %i,ri
			continue
	
	if x==4:
		if r*c == 12 or r*c == 16:
			print 'Case #%d:' %i,ga
			print>>f, 'Case #%d:' %i,ga
			continue
		print 'Case #%d:' %i,ri
		print>>f, 'Case #%d:' %i,ri
		continue

	

