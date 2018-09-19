'''
Codejam template

@author: alarobric
'''

def solve():
	print
	n, k = [int(z) for z in infile.readline().split()]
	print "n, k", n, k
	board = [[] for i in range(n)]
	won = []
	
	for i in range(n):
		line = infile.readline().split()[0]
		for j, char in enumerate(line):
			board[j].append(char)
	for list in board:
		list.reverse()
		
	for row in range(n):
		for i, column in enumerate(board[row]):
			if column == '.':
				tempRow = row
				while tempRow-1>=0:
					board[tempRow][i] = board[tempRow-1][i]
					board[tempRow-1][i] = '.'
					tempRow -= 1
	for list in board:
		print list
		
	#check rows
	current = ''
	streak = 0
	won = []
	for row in range(n):
		for column in range(n):
			if board[row][column] == current:
				streak += 1
				if streak == k-1 and current != '.':
					#print current, "won"
					won.append(current)
			else:
				streak = 0
				current = board[row][column]
		current = ''
		streak = 0
	
	#check columns	
	for column in range(n):
		for row in range(n):
			if board[row][column] == current:
				streak += 1
				if streak == k-1 and current != '.':
					#print current, "won"
					won.append(current)
			else:
				streak = 0
				current = board[row][column]
		current = ''
		streak = 0
	
	#check vertical positive diagonal	
	for row in range(1, n):
		#print "row", row
		current = board[row][0]
		streak = 1
		for i in range(1, row+1):
			#print "try", row+i, i
			if board[row-i][i] == current:
				streak += 1
				if streak == k and current != '.':
					#print current, "won"
					won.append(current)
			else:
				streak = 1
				current = board[row-i][i]
	
	#check horizontal positive diagonal			
	for column in range(1, n-1):
		#print "column", column
		current = board[n-1][column]
		streak = 1
		for i in range(1, n-column):
			#print "try", n-1-i, column+i
			if board[n-1-i][column+i] == current:
				streak += 1
				if streak == k and current != '.':
					#print current, "won"
					won.append(current)
			else:
				streak = 1
				current = board[n-1-i][column+i]
	
	#check vertical negative diagonal			
	for row in range(0, n-1):
		#print "row", row
		current = board[row][0]
		streak = 1
		for i in range(1, n-row):
			#print "try", row+i, i
			if board[row+i][i] == current:
				streak += 1
				if streak == k and current != '.':
					#print current, "won"
					won.append(current)
			else:
				streak = 1
				current = board[row+i][i]
				
	#check horizontal negative diagonal			
	for column in range(1, n-1):
		#print "column", column
		current = board[0][column]
		streak = 1
		for i in range(1, n-column):
			#print "try", i, column+i
			if board[i][column+i] == current:
				streak += 1
				if streak == k and current != '.':
					#print current, "won"
					won.append(current)
			else:
				streak = 1
				current = board[i][column+i]
			
	#print won
	if won.count('R') > 0:
		if won.count('B') > 0:
			return "Both"
		else:
			return "Red"
	if won.count('B') > 0:
		return "Blue"
	return "Neither"

filepath = '/home/alan/Downloads/'
fileprefix = 'A-large' #Change me!

infilename = filepath + fileprefix + '.in'
outfilename = filepath + fileprefix + '.out'
infile = open(infilename, 'rU')
outfile = open(outfilename, 'w+')

numCases = int(infile.readline())
print numCases

for case in range(1, numCases+1):
	str = "Case #%d: %s" %(case, solve())
	print str
	outfile.write(str + "\n")

infile.close()
outfile.close()
