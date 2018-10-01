# tic tac four
import sys

def all_Xs(line):
	for i in range(4):
		if line[i] == 'O' or line[i] == '.':
			return False
	return True

def all_Os(line):
	for i in range(4):
		if line[i] == 'X' or line[i] == '.':
			return False
	return True

#input: four line board
def solve(board, num):
	# Check diagonals
	diag1 = [board[i][i] for i in range(4)]
	diag2 = [board[3-i][i] for i in range(4)]
	print 'Case #' + str(num+1) + ':',
	if all_Xs(diag1) or all_Xs(diag2):
		print 'X won'
		return
	if all_Os(diag1) or all_Os(diag2):
		print 'O won'
		return
	# test all rows and columns
	for i in range(4):
		if all_Xs(board[i]):
			print 'X won'
			return
		if all_Os(board[i]):
			print 'O won'
			return	
		col = [board[j][i] for j in range(4)]
		if all_Os(col):
			print 'O won'
			return
		if all_Xs(col):
			print 'X won'
			return
	for i in range(4):
		for j in range(4):
			if board[j][i] == '.':
				print 'Game has not completed'
				return
	print 'Draw'
	return



def main():
	lines = sys.stdin.readlines()
	N = int(lines[0])
	lines = lines[1:]
	#print lines
	i = 0
	for b in range(N):
		board = lines[i:i+4]
		solve(board, b)
		i += 5
main()