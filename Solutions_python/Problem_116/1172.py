import sys
import string
import time

t0 = time.clock()

try:
	fileInputPointer = open(sys.argv[1], 'r')
	fileOutputPointer = open(sys.argv[2], 'w')
except IOError:
	print("\nInvalid file\n")
	quit()

numberOfCases = int(fileInputPointer.readline().replace('\n',''))
caseNumber = 1
for case in range(0,numberOfCases):
	rowArray = [0,0,0,0]
	columnArray = [0,0,0,0]
	diagonalArray = [0,0]
	emptySquares=0
	for row_number in range(0,4):
		row = fileInputPointer.readline().replace('\n','')
		for column_number in range(0,4):
			if row[column_number]=='X':
				rowArray[row_number]+=1
				columnArray[column_number]+=1
				if row_number==column_number:
					diagonalArray[0]+=1
				elif row_number+column_number==3:
					diagonalArray[1]+=1
			elif row[column_number]=='O':
				rowArray[row_number]-=1
				columnArray[column_number]-=1
				if row_number==column_number:
					diagonalArray[0]-=1
				elif row_number+column_number==3:
					diagonalArray[1]-=1
			elif row[column_number]=='T':
				rowArray[row_number]+=10
				columnArray[column_number]+=10
				if row_number==column_number:
					diagonalArray[0]+=10
				elif row_number+column_number==3:
					diagonalArray[1]+=10
			else:
				emptySquares+=1

	if 4 in rowArray or 13 in rowArray or 4 in columnArray or 13 in columnArray or 4 in diagonalArray or 13 in diagonalArray:
		result = 'X won'
	elif -4 in rowArray or 7 in rowArray or -4 in columnArray or 7 in columnArray or -4 in diagonalArray or 7 in diagonalArray:
		result = 'O won'
	elif emptySquares==0:
		result = 'Draw'
	else:
		result = 'Game has not completed'
	fileOutputPointer.write('Case #'+str(caseNumber)+": "+result+"\n")
	caseNumber+=1
	fileInputPointer.readline()

print("Time: "+str(time.clock()-t0))

