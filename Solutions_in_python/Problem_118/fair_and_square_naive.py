import random
import numpy
import math
import gmpy

def fairSquarableSquareRoot(candidate):
	candidateStr = str(candidate)

	# rubbish if its not a palindrome
	if candidateStr != candidateStr[::-1]:
		return False

	square = candidate ** 2
	squareStr = str(square)
	# rubbish if the square isn't a palindrome
	if squareStr != squareStr[::-1]:
		return False

	return True

cache = set()
def preCacheFairSquarableSquareRoot(start, stop):
	intervalStart = int(math.ceil(math.sqrt(start)))
	intervalStop = int(math.floor(math.sqrt(stop)))
	for candidate in range(1, intervalStop+1):
		if fairSquarableSquareRoot(candidate):
			cache.add(candidate)
preCacheFairSquarableSquareRoot(1, 10e14)

print 'Cache generated'

def solve(start, stop):
	intervalStart = int(math.ceil(math.sqrt(start)))
	intervalStop = int(math.floor(math.sqrt(stop)))
	return len([elem for elem in sorted(cache) if intervalStart <= elem <= intervalStop])

def run():
	output = open('output.txt', 'w')
	input = open('input.txt', 'r')

	numPuzzles = int(input.readline())
	for puzzleId in xrange(1, numPuzzles+1):

		# start processing puzzle #puzzleId
		start, stop =  map(int, input.readline().split())

		result = solve(start, stop)
		print result
		output.write('Case #%s: %s\n' % (puzzleId, result))

	# close input/output
	input.close()
	output.close()

run()