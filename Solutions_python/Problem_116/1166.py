testcases = input()

def checkWon(case):
	xWon, oWon, hasEmptyCell = False, False, False
	
	premuts = []
	for row in case:
		premuts.append(row)
		
	tranpose = ["", "", "" ,""]
	for row in case:
		for colIdx in xrange(0, 4):
			tranpose[colIdx] += row[colIdx]
	
	for row in tranpose:
		premuts.append(row)
	
	diagonal1 = case[0][0] + case[1][1] + case[2][2] + case[3][3]
	diagonal2 = case[3][0] + case[2][1] + case[1][2] + case[0][3]
	
	premuts.append(diagonal1)
	premuts.append(diagonal2)
	
	for premut in premuts:
		xCounter = 0
		oCounter = 0
		tCounter = 0
		emptyCounter = 0
		for c in premut:
			if c == 'X':
				xCounter += 1
			elif c == 'O':
				oCounter += 1
			elif c == 'T':
				tCounter = 1 # Assume there is only 1 T.
			elif c == '.':
				emptyCounter = 1 # Count does not matter. presence does.
			else:
				raise "Unexpected char " + c
		if xCounter + tCounter == 4:
			xWon = True
		if oCounter + tCounter == 4:
			oWon = True
		if emptyCounter > 0:
			hasEmptyCell = True
	
		if xWon or oWon:
			break
	
	someoneWon = xWon or oWon
	gameIsNotOver = not someoneWon and hasEmptyCell
	return xWon, oWon, gameIsNotOver

def processCase(caseNum, case):
	xWon, oWon, notOver = checkWon(case)
	
	if xWon and oWon:
		raise "WTF, both players won"
	
	if xWon:
		status = "X won"
	elif oWon:
		status = "O won"
	elif notOver:
		status = "Game has not completed"
	else:
		status = "Draw"
	
	print("Case #%i: %s" % (caseNum + 1, status))

for caseNum in xrange(0, testcases):
	case = []
	for line in xrange(0, 4):
		case.append(raw_input())
	# Expect empty line
	raw_input()	
	processCase(caseNum, case)
