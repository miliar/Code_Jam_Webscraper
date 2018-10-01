import sys
import math

XWON = "X won"
OWON = "O won"
DRAW = "Draw"
INCOMPLETE = "Game has not completed"
CONT = "Continue"

def main():
	f = open(sys.argv[1])
	T = int(f.readline().strip("\n"))
	for i in range (0,T):
		print "Case #%d: %s" % (i+1, findStatus(f))
		f.readline() #getting rid of empty line!

def parse(x):
	if x=="X": return 1
	if x=="O": return -1
	if x==".": return 0
	if x=="T": return 100

def findWinner(num):
	if num == 4 or num == 103: return XWON
	if num == -4 or num == 97: return OWON
	return CONT

def findStatus(f):
	#create Board
	board = []*4
	isFullBoard = True
	for i in range(4):
		row = list(f.readline().strip("\n"))
		for j in range(4):
			row[j] = parse(row[j])
			if row[j] == 0: isFullBoard = False
		board.append(row)
		
	#find Status
	#check each row
	for i in range(4):
		status = findWinner(sum(board[i]))
		if status != CONT: return status

	#check column
	for i in range(4):
		status = findWinner(sum(zip(*board)[i]))
		if status != CONT: return status

	#check upper left to bottom right diagonal
	total = 0
	for i in range(4):
		total += board[i][i]
	status = findWinner(total)
	if status != CONT: return status

	# check upper right to bottom left diagonal
	total = 0
	for i in range(4):
		total += board[i][3-i]
	status = findWinner(total)
	if status != CONT: return status

	if isFullBoard: return DRAW

	return INCOMPLETE

if __name__ == "__main__":
	main()

