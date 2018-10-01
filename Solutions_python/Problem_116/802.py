import numpy as np
import scipy as sp
import pdb


def player_won(board):

	for i in xrange(4):
		total = board[i,:].sum()
		if total == 4:
			return True
		total = board[:,i].sum()
		if total == 4:
			return True
	
	total = 0
	for i in xrange(4):
		total += board[i,i]
	
	if total == 4:
		return True

	total =0
	for i in xrange(4):
		total += board[i,3-i]
		
	if total == 4:
		return True
	
	return False
	


def evaluate_board(board):

	# did player 1 win:
	#print "board for X:"
	#print np.double(board == 1) + np.double(board <0)
	player1 = player_won(np.double(board == 1) + np.double(board <0))
	if player1:
		return "X won"
		
	player2 = player_won(np.double(board == 2) + np.double(board<0))
	if player2:
		return "O won"
		
	if (board == 0).sum():
		return "Game has not completed"
	else:
		return "Draw"


def run_for_test_case(f   ):

	
	
	board = np.zeros((4,4))
	
	print "\n"
	for i in xrange(4):
		line = f.readline().strip()
		print line
		for j in xrange(4):
			value = 0
			if line[j]  == "T":
				value = -1
			if line[j] == "X":
				value = 1
			if line[j] == "O":
				value = 2
				
			board[i,j] = value
	
	f.readline()
	
	#print board
	output_string = evaluate_board(board)
	#print board
	print "\n",output_string

	return output_string


if __name__ == "__main__":

	f = open ("A-large.in", "r")
	fo = open ("A-large.out","w")
	
	vals = f.readline().strip().split()
	num_test_cases = int(vals[0])
	
	# other values
	

	
	for i in xrange(num_test_cases):
		
		output_string = run_for_test_case(f  )
		fo.write( "Case #"+str(i+1)+": " + output_string + "\n")

