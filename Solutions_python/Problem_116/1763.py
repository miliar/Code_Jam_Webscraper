import numpy as np

INPUT_FILE = "./input1.txt"

CODE = 0
VALUE = 1
D = (".", 0.0)
T = ("T", 0.5)
X = ("X", 10.0)
O = ("O", 11.0)

ITENS = (D, T, X, O)
RESULT = ""

if __name__ == "__main__":

	# input file
	lines = [line.strip() for line in open(INPUT_FILE) if line.strip()]

	print "Total boards: ", lines[0]
	print "Total lines: ", len(lines)

	curPos = 1

	# read boards
	for boardNum in xrange(int(lines[0])):
		RESULT += "Case #" + str(boardNum + 1) + ": "
		print "Parsing board #" + str(boardNum)
		print "Line Position" + str(curPos)

		matrix = []
		inline = []
		for linePos in xrange(curPos, curPos + 4):

			numbers = list(lines[linePos])
			numbers = [D[VALUE] if x == D[CODE] else x for x in numbers]
			numbers = [T[VALUE] if x == T[CODE] else x for x in numbers]
			numbers = [X[VALUE] if x == X[CODE] else x for x in numbers]
			numbers = [O[VALUE] if x == O[CODE] else x for x in numbers]

			#print numbers
			inline.extend(numbers)
			matrix.append(numbers)
			curPos += 1

		#print
		# Calculations
		npMatrix = np.array(matrix)

		results = []
		for l in xrange(4):
			results.append(np.sum(npMatrix[l]))

		for c in xrange(4):
			results.append(np.sum(npMatrix[:, c]))
		
		# diagonals
		results.append(np.sum(np.diag(npMatrix)))
		results.append(npMatrix[0][3] + npMatrix[1][2] + npMatrix[2][1] + npMatrix[3][0])

		#print results

		# Checks
		solved = False
		for result in results:
			if result == (X[VALUE] * 4) or result == (X[VALUE] * 3) + T[VALUE]:
				RESULT += "X won"
				solved = True
				break
			elif result == (O[VALUE] * 4)  or result == (O[VALUE] * 3) + T[VALUE]:
				RESULT += "O won"
				solved = True
				break

		if not solved:
			if D[VALUE] in inline:
				RESULT += "Game has not completed"
			else:
				RESULT += "Draw"

		RESULT += "\n"			

	print "==================================="
	print RESULT
	print "==================================="

	output = open('./output1.txt','w')
	output.write(RESULT)
	output.close()