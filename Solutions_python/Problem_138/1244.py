def main():
	f = file("data.txt")
	numCases = int(f.readline().rstrip())
	for case in xrange(0,numCases):
		bricks = int(f.readline().rstrip())
		naomiBlocks = [float(x) for x in f.readline().rstrip().split()]
		kenBlocks = [float(x) for x in f.readline().rstrip().split()]
		naomiBlocks.sort()
		kenBlocks.sort()
		tempNB = [x for x in naomiBlocks]
		tempKB = [x for x in kenBlocks]
		regularCounter = 0
		decietCounter = 0
		while len(naomiBlocks):
			kenWins = False
			maxVal = naomiBlocks.pop()
			for index, val in enumerate(kenBlocks):
				if val > maxVal: 
					kenWins = True
					kenBlocks.pop(index)
					break
			if kenWins: 
				regularCounter = regularCounter + 1
			else:
				kenBlocks.pop(0)
		regularCounter = bricks - regularCounter
		
		naomiBlocks = tempNB
		kenBlocks = tempKB
		while len(kenBlocks):
			naomiWins = False
			maxVal = kenBlocks.pop()
			for index, val in enumerate(naomiBlocks):
				if maxVal < val: 
					naomiBlocks.pop(index)
					naomiWins = True
					break
			if naomiWins:
				decietCounter = decietCounter + 1
			else:
				naomiBlocks.pop(0)
		
		print "Case #%i: %i %i" % (case + 1,decietCounter,regularCounter)










if __name__ == '__main__':
	main()