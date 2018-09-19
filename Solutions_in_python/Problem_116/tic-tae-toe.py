#!/usr/bin/python

tMatrix = [[' ' for i in range(4)] for j in range(4)]
def main():
	inputFile = open('test.in','r')
	testCases = int(inputFile.readline())

	for i in xrange(testCases):
		for j in range(4):
			line = inputFile.readline().rstrip()
			for c in range(4):
				tMatrix[j][c] = list(line)[c]
		inputFile.readline()
		who = checkWhoWon()
		outputFile = open('test.out','a+')
		outputFile.write('Case #'+str(i+1)+': '+str(who)+'\n')


def checkWhoWon():
	for i in range(4):
		# check rows
		xcount = countXR(i)
		tcount = countTR(i)
		ocount = countOR(i)
		#print 'Row '+str(xcount)+' | '+str(tcount)+' | '+str(ocount)+'\n'
		if xcount == 4 or (xcount+tcount) == 4:
			return 'X won'
		if ocount == 4 or (ocount+tcount) == 4:
			return 'O won'
			
		#check columns
		xcount = countXC(i)
		tcount = countTC(i)
		ocount = countOC(i)
		#print 'Col '+str(xcount)+' | '+str(tcount)+' | '+str(ocount)+'\n'
		if xcount == 4 or (xcount+tcount) == 4:
			return 'X won'
		if ocount == 4 or (ocount+tcount) == 4:
			return 'O won'
			
	#check diagonal 1
	xcount = countXD1()
	tcount = countTD1()
	ocount = countOD1()
	#print str(xcount)+' | '+str(tcount)+' | '+str(ocount)+'\n'
	if xcount == 4 or (xcount+tcount) == 4:
		return 'X won'
	if ocount == 4 or (ocount+tcount) == 4:
		return 'O won'
		
	xcount = countXD2()
	tcount = countTD2()
	ocount = countOD2()
	#print str(xcount)+' | '+str(tcount)+' | '+str(ocount)+'\n'
	if xcount == 4 or (xcount+tcount) == 4:
		return 'X won'
	if ocount == 4 or (ocount+tcount) == 4:
		return 'O won'
			
	for a in range(4):
		for b in range(4):
			if tMatrix[a][b] == '.':
				return 'Game has not completed'
	
	return 'Draw'

def countXR(i):
	count = 0
	for j in range(4):
		if tMatrix[i][j] == 'X':
			count = count + 1
	return count

def countTR(i):
	count = 0
	for j in range(4):
		if tMatrix[i][j] == 'T':
			count = count + 1
	return count
	
def countOR(i):
	count = 0
	for j in range(4):
		if tMatrix[i][j] == 'O':
			count = count + 1
	return count
	
def countXC(i):
	count = 0
	for j in range(4):
		if tMatrix[j][i] == 'X':
			count = count + 1
	return count

def countTC(i):
	count = 0
	for j in range(4):
		if tMatrix[j][i] == 'T':
			count = count + 1
	return count
	
def countOC(i):
	count = 0
	for j in range(4):
		if tMatrix[j][i] == 'O':
			count = count + 1
	return count
	
def countXD1():
	count = 0
	if tMatrix[0][0] == 'X':
		count = count + 1
	if tMatrix[1][1] == 'X':
		count = count + 1
	if tMatrix[2][2] == 'X':
		count = count + 1
	if tMatrix[3][3] == 'X':
		count = count + 1
	return count
	
def countTD1():
	count = 0
	if tMatrix[0][0] == 'T':
		count = count + 1
	if tMatrix[1][1] == 'T':
		count = count + 1
	if tMatrix[2][2] == 'T':
		count = count + 1
	if tMatrix[3][3] == 'T':
		count = count + 1
	return count
	
def countOD1():
	count = 0
	if tMatrix[0][0] == 'O':
		count = count + 1
	if tMatrix[1][1] == 'O':
		count = count + 1
	if tMatrix[2][2] == 'O':
		count = count + 1
	if tMatrix[3][3] == 'O':
		count = count + 1
	return count
	
def countXD2():
	count = 0
	if tMatrix[0][3] == 'X':
		count = count + 1
	if tMatrix[1][2] == 'X':
		count = count + 1
	if tMatrix[2][1] == 'X':
		count = count + 1
	if tMatrix[3][0] == 'X':
		count = count + 1
	return count
	
def countTD2():
	count = 0
	if tMatrix[0][3] == 'T':
		count = count + 1
	if tMatrix[1][2] == 'T':
		count = count + 1
	if tMatrix[2][1] == 'T':
		count = count + 1
	if tMatrix[3][0] == 'T':
		count = count + 1
	return count
	
def countOD2():
	count = 0
	if tMatrix[0][3] == 'O':
		count = count + 1
	if tMatrix[1][2] == 'O':
		count = count + 1
	if tMatrix[2][1] == 'O':
		count = count + 1
	if tMatrix[3][0] == 'O':
		count = count + 1
	return count
	
main()
