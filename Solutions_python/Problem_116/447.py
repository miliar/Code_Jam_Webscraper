import fileinput
import sys

myfile = fileinput.input();
maxboards = 0
currentBoard = 0

for line in myfile:

	if fileinput.isfirstline():
		maxboards = int(line.strip())

	board = []
	domrow = ["T","T","T","T"]
	domcol = ["T","T","T","T"]
	domdiag = ["T","T"]
	notcomplete = False

	currentBoard += 1;
	sys.stdout.write("Case #"+str(currentBoard)+": ")	
	sys.stdout.flush()

	for rowNum in range(4):
		row = myfile.readline().strip()
		board.append(row)

	for row in range(4):
		for col in range(4):

			char = board[row][col]
			diag1 = False
			diag2 = False

			if char == "T":
				continue

			if row == col:
				diag1 = True
			elif (row + col) == 3:
				diag2 = True

			if char == ".":
				notcomplete = True
				domrow[row] = char
				domcol[col] = char
				if diag1:
					domdiag[0] = char
				elif diag2:
					domdiag[1] = char
				continue
			
			if (domrow[row] != char) and (domrow[row] != "T"):
				domrow[row] = "."
			else:
				domrow[row] = char

			if (domcol[col] != char) and (domcol[col] != "T"):
				domcol[col] = "."
			else:
				domcol[col] = char

			if diag1:
				if (domdiag[0] != char) and (domdiag[0] != "T"):
					domdiag[0] = "."
				else:
					domdiag[0] = char
			elif diag2:
				if (domdiag[1] != char) and (domdiag[1] != "T"):
					domdiag[1] = "."
				else:
					domdiag[1] = char				

	for char in domrow+domcol+domdiag:
		if ((char != ".") and (char != "T")):
			print char,"won"
			break
	else:
		if notcomplete:
			print "Game has not completed"
		else:
			print "Draw"

	if maxboards == currentBoard:
		break
