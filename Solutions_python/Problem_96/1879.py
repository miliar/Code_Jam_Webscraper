from math import *

def parseInputFile(name):
	rows = []

	inputFile = open(name, 'r')

	numInputs = int(inputFile.readline())

	for i in range(0, numInputs):
		line = inputFile.readline()
		line = line.strip()
		arrLine = map(lambda x: int(x), line.split())

		rows.append(arrLine)

	return rows;

def printTestCase(id, msg):
	print "Case #%d: %s" % (id, msg)

def dbgPrintData(inputRow):
	print "Input: ", inputRow
	print "Googlers: ", inputRow[0]
	print "Surprises: ", inputRow[1]
	print "Min score: ", inputRow[2]

	for i in range(3, 3 + inputRow[0]):
		print "Score #%d: %d" % (i - 2, inputRow[i])

def calcScore(totalScore):
	avgScr = int(floor(totalScore / 3.0))
	deviation = 0
	remainder = totalScore % 3

	if remainder == 0:
		deviation = 0
	else:
		deviation = remainder

	return [deviation, avgScr]

def isSurprise(val):
	if abs(val) == 2:
		return True
	
	return False

def isAcceptable(inputVal, minVal):
	testVal = inputVal + 2

	if(testVal > 10):
		testVal = 10


	return (testVal >= minVal)

def solveProblem(inputRow):
	#dbgPrintData(inputRow)

	numGooglers = inputRow[0]
	numSurprises = inputRow[1]
	minScore = inputRow[2]

	scr = []

	okScore = []
	surpriseScores = []

	#print "Expected: ", numSurprises

	for i in range(3, 3 + numGooglers):
		if inputRow[i] == 0:
			if(minScore == 0):
				okScore.append([0, 0])

		else:
			scr = calcScore(inputRow[i])

			if scr[1] >= minScore:
				okScore.append(scr)
			else:
				if scr[0] == 0:
					if scr[1] + 1 >= minScore:
						if numSurprises > 0:
							numSurprises = numSurprises -1
							okScore.append(scr)
				else:
					surpriseScores.append(scr)
	
	surpriseScores.sort(key = lambda x: abs(x[0]), reverse = True)

	for i in range(len(surpriseScores)):
		currScore = surpriseScores[i]

		if numSurprises > 0:
			if (currScore[1] + currScore[0]) >= minScore:
				okScore.append(currScore)
				numSurprises = numSurprises - 1

		else:
			if (currScore[1] + 1) >= minScore:
				okScore.append(currScore)
	
	#print inputRow
	#print "OK: ", okScore

	return len(okScore)

def SolveCodeJam(fileName):
	parsedLines = parseInputFile(fileName)

	for i in range(len(parsedLines)):
		printTestCase(i + 1, solveProblem(parsedLines[i]))

#print solveProblem([3, 1, 5, 15, 13 ,11])
#print solveProblem([3, 0, 8, 23, 22, 21])
#print solveProblem([2, 1, 1, 8, 0])
#print solveProblem([6, 2, 8, 29, 20, 8, 18, 18,21])
#print solveProblem([3, 0, 8 ,23, 22, 21])
#print solveProblem([1, 0, 8, 21])

#SolveCodeJam("b_test.in")
SolveCodeJam("B-small-attempt3.in")