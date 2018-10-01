T = int( raw_input().strip() )
for testCase in xrange(1, T+1):
	Raw = raw_input().strip().split()
	N = int( Raw[0] ) 
	Latest = [0, 0]
	Position = [1, 1]
	for i in xrange( N ):
		ch = str( Raw[i*2+1] )
		pos = int( Raw[i*2+2] ) 
		if ch == "O" : robot = 0
		else: robot = 1
		
		Latest[robot] = max( Latest[1^robot], Latest[robot] + abs( pos - Position[robot] ) ) + 1
		Position[robot] = pos
			
	print "Case #" + str(testCase) + ":", max( Latest )