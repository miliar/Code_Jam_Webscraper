import sys
import math


def sortstr(comb_):
    return ''.join(sorted(comb_))

f = open(sys.argv[1])
lines = f.readlines()
f.close()

i = 1
t = int(lines[0])

xwonPattern = {"XXXX", "TXXX", "XTXX", "XXTX", "XXXT"}
owonPattern = {"OOOO", "TOOO", "OTOO", "OOTO", "OOOT"}

for tt in range(t):
	xwon = False;
	owon = False;
	result = ""
	hasDot = False
	board = []
	for b in range(0, 4):
		if (not hasDot) and (lines[i].find(".") != -1):
			hasDot = True
		board.append(lines[i].strip())
		i += 1

	for b in range(0, 4):
		board.append(board[0][b] + board[1][b] + board[2][b] + board[3][b])

	board.append(board[0][0] + board[1][1] + board[2][2] + board[3][3])
	board.append(board[3][0] + board[2][1] + board[1][2] + board[0][3])

	for line in board:
		if (not xwon) and (line in xwonPattern):
			xwon = True
			#print("xwon: " + line)
		if (not owon) and (line in owonPattern):
			owon = True
			#print("owon: " + line)

	if (xwon):
		if (owon):
			result = "Draw"
		else:
			result = "X won"
	elif (owon):
		result = "O won"
	elif (hasDot):
		result = "Game has not completed"
	else:
		result = "Draw"

	print ("Case #" + str(tt+1) + ": " + result)
	i = i+1
