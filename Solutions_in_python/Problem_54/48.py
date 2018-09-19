def gcd(x,y):
	g = y
	while x != 0:
		g = x
		x = y % x
		y = g
	return g

c = int(raw_input())

for casenum in range(1,c+1):
	t=raw_input().split();
	t=list(set(t[1:]));
	n=len(t);
	
	g=int(t[1])-int(t[0]);
	for j in range(1,n-1):
		g=gcd( g, int(t[j+1])-int(t[0]) )
	
	if g < 0:
		g = -g
	
	print 'Case #%d: %d' % (casenum, (g-int(t[0])%g)%g)

