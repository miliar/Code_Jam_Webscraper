import math
import sys,os


#6
#XXXT
#....
#OO..
#....

file = open(sys.argv[1],'r')
file.readline()

currentBoard = []
currentCase = 1

for line in file:
	if line == '\n':
		#solve
		complete = 0		
		winner = 0

		print "Case #"+str(currentCase)+": ",
		currentCase += 1

#		print currentBoard

		columns = [[],[],[],[]]

		j = 0
		diag1 = ''
		diag2 = ''
		dots = 0
		for row in currentBoard:
			if row.count('X')+row.count('T') == 4:
				winner = 'X' #print "X won"
				complete = 1
			if row.count('O')+row.count('T') == 4:
                                winner = 'O' #print "O won"
				complete = 1
			for i in [0,1,2,3]:
				columns[i].append(row[i])
			diag1 += row[j]
			diag2 += row[3-j]
			j+=1
			dots += row.count('.')
#			print diag1, diag2

#		print columns

		for col in columns:
			if col.count('X')+col.count('T') == 4:
                                winner = 'X' #print "X won"
				complete = 1
                        if col.count('O')+col.count('T') == 4:
                                winner = 'O' #print "O won"
				complete = 1

#		print diag1,diag2
		
		if diag1.count('X')+diag1.count('T') == 4:
			winner = 'X' #print "X won"
			complete = 1
		if diag2.count('X')+diag2.count('T') == 4:
			winner = 'X' #print "X won"
			complete = 1

		if diag1.count('O')+diag1.count('T') == 4:
                        winner = 'O' #print "O won"
			complete = 1
                if diag2.count('O')+diag2.count('T') == 4:
                        winner = 'O' #print "O won"
			complete = 1
		if winner:
			print winner+" won"

#		print dots
		if complete == 0 and dots == 0:
			print "Draw"
			complete = 1
		if complete == 0:
			print "Game has not completed"


		currentBoard = []
	else:
		currentBoard.append(line.strip())


