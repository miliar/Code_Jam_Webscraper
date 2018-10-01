#

C = int( raw_input() )

for t in xrange( 1, C+1 ):
	
	N = int( raw_input() )
	
	x = [0]*N
	y = [0]*N
	r = [0]*N
	
	for i in xrange( N ):
		
		x[i], y[i], r[i] = map( float, raw_input().split() )
	
	if N == 1:
		
		print "Case #%d: %f" % (t, r[0])
	
	elif N == 2:
		
		print "Case #%d: %f" % (t, max( r[0], r[1] ))
	
	elif N == 3:
		
		a = max( r[0], (((x[1]-x[2])**2+(y[1]-y[2])**2)**0.5+r[1]+r[2])/2 )
		b = max( r[1], (((x[0]-x[2])**2+(y[0]-y[2])**2)**0.5+r[0]+r[2])/2 )
		c = max( r[2], (((x[1]-x[0])**2+(y[1]-y[0])**2)**0.5+r[1]+r[0])/2 )
		
		print "Case #%d: %f" % (t, min( a, b, c ))
		
	else:
		
		print "Case #%d: FAIL" % (t)
