from math import sqrt
C = int(raw_input())
for t in xrange(C):
	N = int(raw_input())
	plants = [map(int, raw_input().split()) for i in xrange(N)]
	if (N>3):
		print "0.000000"
		continue
	ans = 10000000000000
	if (N==1): ans=plants[0][2]
	if (N==2): ans = max( plants[0][2], plants[1][2] )
	if (N==3):
		for a, b, c in ((0, 1, 2), (0, 2, 1), (1, 2, 0)):
			r1 = (sqrt( (plants[a][0]-plants[b][0])**2.0 + (plants[a][1]-plants[b][1])**2.0) + (plants[a][2] + plants[b][2]))/2.0
			r2 = plants[c][2]
			ans = min(max(r1, r2), ans)
	print 'Case #%d: %.6f' % (t+1, ans)
		
	
