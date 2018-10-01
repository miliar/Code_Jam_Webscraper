import math

def readInput(filename):
	# reads the input and returns the number of cases and a list of (s,k) tuples
	with open(filename) as file:
		firstLineRead = False
		numCases = 0
		cases = []
		for line in file:
			lineString = line.rstrip()
			if not firstLineRead:
				numCases = int(lineString)
				firstLineRead = True
			else:
				n,k = lineString.split(' ')
				cases.append((int(n),int(k)))
	return numCases, cases

def solve(n, k):
	# max(ls, rs) is always going to be within 1 of min(ls, rs); otherwise, the person could raise min(ls,rs) by moving either left or right.
	# the people coming in are going to do binary splits of the empty stalls, since they will maximize the number of stalls to their left and right.
	# by counting how many times the existing blocks of empty stalls have been chopped in half (i.e., our depth on the binary tree),
	# we can calculate the size of the largest possible remaining block of empty stalls, which we know the last person will want to take
	# from there, calculating ls and rs is trivial, since we just take one of the empty stalls and chop the remainder in half

	# find out what splitting level we're on
	splits = int(math.floor(math.log(k, 2)))

	# calculate the size of the largest possible remaining stall block
	largestContiguousStalls = n
	for i in range(splits):
		largestContiguousStalls = int(math.ceil((largestContiguousStalls - 1)/2))

	# it is possible that, during the current split, all of the largest contiguous stall blocks have been occupied, which
	# would place the next person in a stall block of size largestContiguousStalls - 1.
	# we need to calculate how many blocks of size largestContiguousStalls existed at the last split, and how
	# many people came in since the last split completed
	stallsAvailableAtLastSplit = n - (2**splits-1)
	numBlocks = 2**splits
	# we know that every contiguous stall block, at the time the last split completed, had either largestContiguousStalls or largestContiguousStalls-1 stalls.
	# we can calculate how many stalls and how many contiguous blocks were empty at the time the last split completed
	# we solve a system of equations as follows:
	# stallsAvailableAtLastSplit = largestContiguousStalls*(number of LCS sized blocks) + (largestContiguousStalls-1)*(number of LCS-1 sized blocks)
	# numBlocks = (number of LCS sized blocks) + (number of LCS-1 sized blocks)
	# we solve for (number of LCS sized blocks), and we get the below answer
	numberLCSSizedBlocks = stallsAvailableAtLastSplit + numBlocks - largestContiguousStalls*numBlocks
	# if the number of people since the last split is >= this number, then the largest block of free stalls now is actually one stall smaller than we predicted
	peopleSinceLastSplit = (k-1) - (2**(splits)-1)
	if peopleSinceLastSplit >= numberLCSSizedBlocks:
		largestContiguousStalls -= 1


	# calculate and return ls and rs
	stallsLeft = largestContiguousStalls - 1
	return math.ceil(stallsLeft / 2), math.floor(stallsLeft / 2)


if __name__ == '__main__':
	numCases, cases = readInput('C-small-2-attempt0.in')

	# open output file
	with open('output.out', 'w') as outputFile:

		# solve each case
		for i, (n, k) in enumerate(cases):
			result = solve(n, k)

			# write results
			outputFile.write('Case #{0}: {1} {2}\n'.format(i+1, result[0], result[1]))
