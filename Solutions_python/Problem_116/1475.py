import numpy

f = open('/tmp/test','r')
m = f.readlines()
N = int(m[0])
lineCount = int()

lineCount += 1
for k in range(N):
	game = [m[lineCount],m[lineCount+1],m[lineCount+2],m[lineCount+3]]
	sumXH = numpy.zeros(4)
	sumXV = numpy.zeros(4)
	sumOH = numpy.zeros(4)
	sumOV = numpy.zeros(4)
	diagX1 = 0
	diagX2 = 0
	diagO1 = 0
	diagO2 = 0

	emptySpace = False
	completed = False

	xWon = False
	oWon = False

	for i in range(4):
		for j in range(4):
			if game[i][j] == 'X':
				sumXH[i] += 1
				sumXV[j] += 1
			if game[i][j] == 'O':
				sumOH[i] += 1
				sumOV[j] += 1
			if game[i][j] == 'T':
				sumXH[i] += 1
				sumXV[j] += 1
				sumOH[i] += 1
				sumOV[j] += 1
			if game[i][j] == '.':
				emptySpace = True

	for i in range(4):
		if game[i][i] == 'X' or game[i][i] == 'T':
			diagX1 += 1
		if game[i][3-i] == 'X' or game[i][3-i] == 'T':
			diagX2 += 1
		if game[i][i] == 'O' or game[i][i] == 'T' :
			diagO1 += 1
		if game[i][3-i] == 'O' or game[i][3-i] == 'T':
			diagO2 += 1

		if sumXH[i] == 4 or sumXV[i] == 4:
			xWon = True
			break
		if sumOH[i] == 4 or sumOV[i] == 4:
			oWon = True
			break


	if diagX1 == 4 or diagX2 == 4:
		xWon = True
	if diagO1 == 4 or diagO2 == 4:
		oWon = True

	if xWon:
		print 'Case #'+str(k+1)+': X won'
	elif oWon:
		print 'Case #'+str(k+1)+': O won'
	elif emptySpace:
		print 'Case #'+str(k+1)+": Game has not completed" 
	else:
		print 'Case #'+str(k+1)+": Draw" 

	lineCount += 5





