import os, sys

T = int( raw_input().rstrip() )

for i in xrange(T):

	values = raw_input().rstrip().split(' ')
	C = float( values[0] )
	F = float( values[1] )
	X = float( values[2] )

	total_time = 0.0
	rate = 2.0

	finished = False

	while( not finished ):
		time_with_new_farm 	= C/rate + X/(rate + F)
		time_to_X 					= X/rate
		if( time_with_new_farm < time_to_X ):
			total_time 	+= C/rate
			rate 				+= F
		else:
			total_time 	+= time_to_X
			finished 		= True

	print "Case #%s: %s" % (i+1, total_time)
