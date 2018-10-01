import sys

input = open(sys.argv[1], 'r')

def validate_pos(player, pos):
	return ((pos == player) or (pos == 'T'))

def validate_win(player, board):
	for row in range(0, 4):
		for col in range(0, 4):
		
			col_matches = 0
			for col_index in range(0, 4):
				if (validate_pos(player, board[row][col_index])):
					col_matches += 1
			if (col_matches == 4):
				return True
				
			row_matches = 0
			for row_index in range(0, 4):
				if (validate_pos(player, board[row_index][col])):
					row_matches += 1
			if (row_matches == 4):
				return True
								
			if (row == col):
				diag1_matches = 0
				for diag1_index in range(0, 4):
					if (validate_pos(player, board[diag1_index][diag1_index])):
						diag1_matches += 1
				if (diag1_matches == 4):
					return True
			
			if (row + col == 3):
				diag2_matches = 0
				for diag2_index in range(0, 4):
					if (validate_pos(player, board[diag2_index][3 - diag2_index])):
						diag2_matches += 1
				if (diag2_matches == 4):
					return True
			
	return False

def has_empty_cells(board):
	for row in range(0, 4):
		for col in range(0, 4):
			if (board[row][col] == '.'):
				return True
	return False

#

n = input.readline()
n = n[:-1]
n = int(n)

for i in range(0, n):
	board = []	
	for j in range(0, 4):
		line = input.readline()
		line = line[:-1]
		board.append(line)
	input.readline()

	sys.stdout.write('Case #' + str(i + 1) + ': ')
	
	x_wins = validate_win('X', board)
	o_wins = validate_win('O', board)

	if (x_wins and o_wins):
		sys.stdout.write('Draw')
	elif (x_wins):
		sys.stdout.write('X won')
	elif (o_wins):
		sys.stdout.write('O won')
	else:
		if (has_empty_cells(board)):
			sys.stdout.write('Game has not completed')
		else:
			sys.stdout.write('Draw')
			
	if (i + 1 < n):
		print('')

input.close()