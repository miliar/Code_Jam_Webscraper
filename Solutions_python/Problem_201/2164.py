inputName = input("> ")
inputFile = open(inputName, "r")
outputFile = open("bathroomOut.txt", "w")

def leftSide(ind, values):
	count = 0
	for i in range(ind - 1, -1, -1):
		if values[i] == True:
			break
		count += 1
	return count

def rightSide(ind, values):
	count = 0
	for i in range(ind + 1, len(values)):
		if values[i] == True:
			break
		count += 1
	return count

def gapSize(ind, values):
	count = 0
	for i in range(ind, len(values)):
		if values[i] == True:
			break
		count += 1
	return count

testCases = int(inputFile.readline())
for i in range(testCases):
	print(str(i))
	inLine = inputFile.readline().split()
	numStalls = int(inLine[0])
	numPeople = int(inLine[1])
	stalls = [True] + [False] * numStalls + [True]
	if numPeople == numStalls:
		if i < testCases - 1:
			outputFile.write("Case #" + str(i + 1) + ": 0 0\n")
		else:
			outputFile.write("Case #" + str(i + 1) + ": 0 0")
		continue
	for j in range(numPeople):
		'''
		bestInd = 0
		for k in range(1, numStalls + 1):
			if stalls[k] == False:
				bestInd = k
				break
		k = bestInd + 1
		while k < numStalls + 1:
			if stalls[k] == False:
				leftK = leftSide(k, stalls)
				rightK = rightSide(k, stalls)
				leftBest = leftSide(bestInd, stalls)
				rightBest = rightSide(bestInd, stalls)
				if min(leftK, rightK) > min(leftBest, rightBest):
					bestInd = k
				elif min(leftK, rightK) == min(leftBest, rightBest) and max(leftK, rightK) > max(leftBest, rightBest):
					bestInd = k
				if bestInd != k:
					for l in range(k + 1, numStalls + 1):
						if stalls[l - 1] == True and stalls[l] == False:
							k = l - 1
			k += 1
		stalls[bestInd] = True
		if j == numPeople - 1:
			if i < testCases - 1:
				outputFile.write("Case #" + str(i + 1) + ": " + str(max(leftSide(bestInd, stalls), rightSide(bestInd, stalls))) + " " + str(min(leftSide(bestInd, stalls), rightSide(bestInd, stalls))) + "\n")
			else:
				outputFile.write("Case #" + str(i + 1) + ": " + str(max(leftSide(bestInd, stalls), rightSide(bestInd, stalls))) + " " + str(min(leftSide(bestInd, stalls), rightSide(bestInd, stalls))))
		'''
		largestGapStart = 0
		largestSize = 0
		for k in range(1, numStalls + 1):
			if stalls[k] == False:
				largestGapStart = k
				largestSize = gapSize(largestGapStart, stalls)
				break
		for k in range(largestGapStart + 1, numStalls + 1):
			thisOne = gapSize(k, stalls)
			if thisOne > largestSize:
				largestGapStart = k
				largestSize = thisOne
				
		if largestSize % 2 == 0:
			chosenPlace = largestGapStart + (largestSize / 2) - 1
		else:
			chosenPlace = largestGapStart + (largestSize - 1) / 2
		chosenPlace = int(chosenPlace)
		stalls[chosenPlace] = True
		if j == numPeople - 1:
			if i < testCases - 1:
				outputFile.write("Case #" + str(i + 1) + ": " + str(max(leftSide(chosenPlace, stalls), rightSide(chosenPlace, stalls))) + " " + str(min(leftSide(chosenPlace, stalls), rightSide(chosenPlace, stalls))) + "\n")
			else:
				outputFile.write("Case #" + str(i + 1) + ": " + str(max(leftSide(chosenPlace, stalls), rightSide(chosenPlace, stalls))) + " " + str(min(leftSide(chosenPlace, stalls), rightSide(chosenPlace, stalls))))
outputFile.close()