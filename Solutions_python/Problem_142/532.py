def MakeShortest(sWord):
	sShort = sWord[0]
	nIdx = 1
	while (nIdx < len(sWord)):
		if sWord[nIdx] != sWord[nIdx - 1]:
			sShort += sWord[nIdx]
			
		nIdx += 1
		
	return sShort
	
def IsPossible(lChoices):
	lShorts = [MakeShortest(x) for x in lChoices]
	
	return len(lChoices) == len(filter(lambda x: x == lShorts[0], lShorts))
	
def GetBatch(sWord):
	sBatch = sWord[0]
	nIdx = 1
	while (nIdx < len(sWord)) and (sWord[nIdx] == sWord[nIdx - 1]):
		sBatch += sWord[nIdx]
		
		nIdx += 1
		
	return sBatch
	
def Choices(lChoices):
	sOutput = ""
	nMoves = 0
	
	while (lChoices[0] != ""):
		lCurrentBatch = []
		
		for sChoice in lChoices:
			lCurrentBatch += [GetBatch(sChoice)]
		
		# Calculate the number of appearances of this char's batch
		nAvgAppearance = reduce(lambda x, y: x + y, [len(x) for x in lCurrentBatch]) / len(lChoices)
		
		for sBatch in lCurrentBatch:
			nMoves += abs(len(sBatch) - nAvgAppearance)
			
		lNewChoices = []
			
		# Cut out the batches
		for sBatch, sChoice in zip(lCurrentBatch, lChoices):
			lNewChoices += [sChoice[len(sBatch):]]
			
		lChoices = lNewChoices
		
	return nMoves
	
nTestCases = int(raw_input())
for i in xrange(nTestCases):
	nStrings = int(raw_input())
	
	lPossibility = []
	
	for nStringIdx in xrange(nStrings):
		lPossibility += [raw_input()]

	if not IsPossible(lPossibility):
		print "Case #%d: Fegla Won" % (i + 1)
	else:
		print "Case #%d: %d" % (i + 1, Choices(lPossibility))