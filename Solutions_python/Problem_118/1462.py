#!/usr/bin/python
import math

####### SET TO FALSE BEFORE SUBMITTING ########
debugOutput = False
##############################################

maxTestCases = int(raw_input().strip())
fairSquareCount = 0

##########################################################################
# FUNCTIONS
##########################################################################

def findFairSquares(minNum, maxNum):
	totalCount = 0

	#Converting to long so we don't blow up on a large dataset sys.maxint <= A <= B <= 10^100
	squareMinCeil = long(math.ceil(math.sqrt(minNum)))
	squareMaxFloor = long(math.sqrt(maxNum))

	for x in xrange(squareMinCeil, squareMaxFloor+1):
		if debugOutput:
			print "-- {} ({})".format(x*x, x), 

		if isPalin(x) and isPalin(x*x):
			totalCount += 1

			if debugOutput:
				print "*", 

		if debugOutput:
			print 

	return totalCount

#	return len(filter(isPalin, map(lambda x: x*x, xrange(squareMinCeil, squareMaxFloor))))

#-------------------------------------------------------------------------
def isPalin(n):
	s = str(n)

	#Pythonic string reversal using slice notation instead of looping a character swap that meets in the middle
	reverseStr = s[::-1]

	return (s == reverseStr)

#**************************************************************************
# END FUNCTIONS
#**************************************************************************
if debugOutput:
	print maxTestCases

for testCase in xrange(1, maxTestCases+1):
	fairSquareCount = 0
	minNum, maxNum = map(long, raw_input().strip().split(' '))
	
	if debugOutput:
		print minNum, maxNum 
	
	print "Case #{}: {}".format(testCase, findFairSquares(minNum, maxNum))

	if debugOutput:
		print 
