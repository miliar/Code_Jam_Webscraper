#! /usr/bin/env python

from collections import deque
import sys

fileIn = open('A-small-attempt1.in','r')
fileOut = open('output.out', 'w')

testCases = int(fileIn.readline())
results = deque()

for i in range(testCases):
	diagonalLeftRight = 1
	diagonalRightLeft = 1
	row = [1 for x in xrange(4)]
	column = [1 for x in xrange(4)]
	resultString = "Case #" + str(i+1) + ": Draw"
	hash = 0
	#Case i:
	for j in range(4):
		#one line
		line = fileIn.readline()	
		for k in range(4):
			multiple = 1
			if (line[k] == 'X'):
				hash = 10
			elif (line[k] == 'O'):
				hash = -10
			elif (line[k] == 'T'):
				hash = 0
				multiple = 1.1
			else:
				#possible game hasn't been completed
				hash = 0
				multiple = 0
				resultString = "Case #" + str(i+1) + ": Game has not completed"
			#update sum of the row:	
			row[j] = (row[j] + hash)*multiple
			#update diagonals:
			if (k == j):
				diagonalLeftRight = (diagonalLeftRight + hash)*multiple
			elif ((k+j) == 3):
				diagonalRightLeft = (diagonalRightLeft + hash)*multiple
			#update sum of collumns
			column[k] = (column[k] + hash)*multiple
	
	#check for solutions
	#diagonals:
	if ((diagonalLeftRight > 30) | (diagonalRightLeft > 30)):
		resultString = "Case #" + str(i+1) + ": X won"
		
	elif ((diagonalLeftRight < -30) | (diagonalRightLeft < -30)):
		resultString = "Case #" + str(i+1) + ": O won"
	
	#rows	
	for k in range(len(row)):
		if (row[k] > 30):
			resultString = "Case #" + str(i+1) + ": X won"
		if (row[k] < -30):
			resultString = "Case #" + str(i+1) + ": O won"	
			
	for k in range(len(column)):
		if (column[k] > 30):
			resultString = "Case #" + str(i+1) + ": X won"
		if (column[k] < -30):
			resultString = "Case #" + str(i+1) + ": O won"		
	
	results.append(resultString)
	#new line then done:
	line = fileIn.readline()
	
#print results	
for i in range(testCases):
	fileOut.write(results.popleft() + "\n") 

fileIn.close()
fileOut.close()