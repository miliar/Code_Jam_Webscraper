#

T = int( raw_input() )

for t in xrange( 1, T+1 ):
	
	P = int( raw_input() )
	
	miss = map( int, raw_input().split() )
	
	for p in xrange( P ):
		
		raw_input() # should all be 1s for small test case
	
	viewing = set()
	
	for i in xrange( 1<<P ):
		
		value = i+4096
		value >>= miss[i]
		for j in xrange( miss[i], P ):
			
			value >>= 1
			viewing.add( value )
			#print i, value
	
	print "Case #%d: %d" %(t, len(viewing))
