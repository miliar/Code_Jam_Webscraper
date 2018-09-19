#!/usr/bin/env python


# Get the number of test cases.
T = int( raw_input() )
# Process each test case.
for case in range( 1, T + 1 ):
	# Get the number of files and the capacity of each disc.
	NandX = raw_input().split()
	N = int( NandX[ 0 ] )
	X = int( NandX[ 1 ] )
	# Perform some data structure initialization.
	countBySize = []
	for _ in range( 0, 701 ):
		countBySize.append( 0 )
	fileSizes = set()
	filesLeft = N
	discsUsed = 0
	# Get the size of each file and populate our data structures.
	line = raw_input().split()
	for fileIndex in range( 0, N ):
		S = int( line[ fileIndex ] )
		if S not in fileSizes:
			fileSizes.add( S )
		countBySize[ S ] += 1
	# Store the files to the discs.
	while filesLeft > 0:
		discsUsed += 1
		capacity = X
		# Store the largest remaining file first.
		sortedSizes = sorted( fileSizes, reverse=True )
		chosen = sortedSizes[ 0 ]
		capacity -= chosen
		countBySize[ chosen ] -= 1
		if countBySize[ chosen ] < 1:
			fileSizes.remove( chosen )
		filesLeft -= 1
		# Move to the next disc if the current one is out of space.
		if capacity < 1:
			continue
		# Store a second file by choosing the largest file that
		# can fit in the remaining space on the current disc.
		sortedSizes = sorted( fileSizes, reverse=True )
		for candidate in sortedSizes:
			if candidate > capacity:
				continue
			countBySize[ candidate ] -= 1
			if countBySize[ candidate ] < 1:
				fileSizes.remove( candidate )
			filesLeft -= 1
			break
	print "Case #%d: %d" % ( case, discsUsed )

