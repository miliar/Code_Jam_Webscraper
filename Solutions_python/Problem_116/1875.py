import sys

def main():
	inputFile = sys.argv[1]
	f = open(inputFile, "r")
	o = open("output.txt", "w")
	numOfTestCases = int(f.readline()[:-1])
	gameBoard = []
	result = []
	for x in range(numOfTestCases):
		gameBoard = []
		for y in range(4):
			if x == numOfTestCases - 1 and y == 3:
				line = f.readline()
			else:
				line = f.readline()[:-1]
			gameBoard.append(line)
		# Skip the empty line...
		if not x == numOfTestCases - 1:
			f.readline()
		# check rows
		result = []
		print gameBoard
		for k in range(4):
			result.append(checkComb(gameBoard[k]))
		result.append(checkComb([gameBoard[0][0], gameBoard[1][0], gameBoard[2][0], gameBoard[3][0]]))
		result.append(checkComb([gameBoard[0][1], gameBoard[1][1], gameBoard[2][1], gameBoard[3][1]]))
		result.append(checkComb([gameBoard[0][2], gameBoard[1][2], gameBoard[2][2], gameBoard[3][2]]))
		result.append(checkComb([gameBoard[0][3], gameBoard[1][3], gameBoard[2][3], gameBoard[3][3]]))
		result.append(checkComb([gameBoard[0][0], gameBoard[1][1], gameBoard[2][2], gameBoard[3][3]]))
		result.append(checkComb([gameBoard[3][0], gameBoard[2][1], gameBoard[1][2], gameBoard[0][3]]))
		message = "Draw"
		for m in result:
			if m == 'X':
				message = "X won"
				break
			elif m == 'O':
				message = "O won"
				break
			elif m == "incomplete":
				message = "Game has not completed"
		o.write("Case #" + str(x + 1) + ": " + message + "\n")



def checkComb(line):
	X = 0
	O = 0
	T = 0
	for i in range(len(line)):
		temp = line[i]
		if temp == 'X':
			X = X + 1
		elif temp == 'O':
			O = O + 1
		elif temp == 'T':
			T = T + 1
		elif temp == '.':
			# incomplete
			return "incomplete"
	if X == 4 or (X == 3 and T == 1):
		return "X"
	if O == 4 or (O == 3 and T == 1):
		return "O"
	else:
		return "draw"












if __name__ == "__main__":
    main()