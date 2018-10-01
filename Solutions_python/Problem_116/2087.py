def getGameBoards(inputFileName):
	gameBoards = []

	with open(inputFileName, 'r') as inputFile:
		testCases = int(inputFile.readline())

		for testCaseNum in range(testCases):
			gameBoard = []

			for gameBoardLine in range(4):
				lineList = list(inputFile.readline()[:4])
				gameBoard.append(lineList)

			gameBoards.append(gameBoard)
			inputFile.readline() # empty line

	return gameBoards

def isPlayerWon(gameBoard, signPlayer):
	global signSpecial

	# rows
	for rowNum in range(4):
		for colNum in range(4):
			if (gameBoard[rowNum][colNum] != signPlayer
				and gameBoard[rowNum][colNum] != signSpecial) :
				break
		else:
			return True
	# cols
	for colNum in range(4):
		for rowNum in range(4):
			if (gameBoard[rowNum][colNum] != signPlayer
				and gameBoard[rowNum][colNum] != signSpecial) :
				break
		else:
			return True
	# diagonal left
	for rowAndColNum in range(4):
		if (gameBoard[rowAndColNum][rowAndColNum] != signPlayer
			and gameBoard[rowAndColNum][rowAndColNum] != signSpecial) :
			break
	else:
		return True
	# diagonal right
	for rowAndColNum in range(4):
		if (gameBoard[rowAndColNum][3 - rowAndColNum] != signPlayer
			and gameBoard[rowAndColNum][3 - rowAndColNum] != signSpecial) :
			break
	else:
		return True

	return False

def isUnfilledField(gameBoard):
	global signEmpty

	for rowNum in range(4):
		for colNum in range(4):
			if (gameBoard[rowNum][colNum] == signEmpty):
				return True

	return False

def writeOutput(outputFileName, content):
	 with open(outputFileName, 'w') as outputFile:
	 	outputFile.write(content)

#------------------------------------------------------------------------------

output = '';
signSpecial = 'T'
signPlayerX = 'X'
signPlayerO = 'O'
signEmpty = '.'
gameBoards = getGameBoards('input')

for (counter, gameBoard) in enumerate(gameBoards):
	actResult = ''

	if (isPlayerWon(gameBoard, signPlayerX)):
		actResult = 'X won'
	elif (isPlayerWon(gameBoard, signPlayerO)):
		actResult = 'O won'
	elif (isUnfilledField(gameBoard)):
		actResult = 'Game has not completed'
	else:
		actResult = 'Draw'

	output += "Case #{0}: {1}\n".format(counter + 1, actResult)

writeOutput('output', output)
