#!/usr/bin/python

#imports
from sys import argv
from sys import exit

#functions
def read_input(file_name):
	try:
		input_file = open(file_name, 'r')
		input_data = input_file.read()
		input_file.close()
		input_data = input_data.split("\n")
	except:
		print "Cannot read file: {}".format(input_file)
		exit(1)
	return input_data

def parse_input(input_list):
	num_cases = input_list[0]
	cases = [[]]
	for i in range(1, len(input_list)):
		if input_list[i] == '':
			cases.append([])
			continue
		cases[-1].append(input_list[i])
	return num_cases, cases

def horizontal_win(board):
	winner = False
	for line in board:
		if not '.' in line and not 'O' in line:
			winner = "X"
			break
		if not '.' in line and not 'X' in line:
			winner = "O"
			break
	return winner

def vertical_win(board):
	winner = False
	#create the vertical lines
	for i in range(len(board)):
		vert_line = []
		for j in range(len(board[0])):
			vert_line.append(board[j][i])
		if not '.' in vert_line and not 'O' in vert_line:
			return "X"
		if not '.' in vert_line and not 'X' in vert_line:
			return "O"
	return winner

def diag_win(board):
	winner = False
	ltr = []
	for i in range(4):
		try:
			ltr.append(board[i][i])
		except:
			print board
			exit(1)
	if not '.' in ltr and not 'O' in ltr:
		return "X"
	if not '.' in ltr and not 'X' in ltr:
		return "O"
	rtl = [] # 03 12 21 30
	for i in range(3, -1, -1):
		rtl.append(board[3 - i][i])
	if not '.' in rtl and not 'O' in rtl:
		return "X"
	if not '.' in rtl and not 'X' in rtl:
		return "O"
	return winner

def determine_winners(game_boards):
	results = []
	for board in game_boards:
		# check horizontal wins
		hw = horizontal_win(board)
		if hw == "X":
			results.append("X won")
			continue
		elif hw == "O":
			results.append("O won")
			continue
		# check vertical wins
		vw = vertical_win(board)
		if vw == "X":
			results.append("X won")
			continue
		elif vw == "O":
			results.append("O won")
			continue
		# check diaganols
		dw = diag_win(board)
		if dw == "X":
			results.append("X won")
			continue
		elif dw == "O":
			results.append("O won")
			continue
		# check for draw
		all_lines = ''
		for line in board:
			all_lines += ''.join(line)
		if not '.' in all_lines:
			results.append("Draw")
			continue
		# no winner if empties
		results.append("Game has not completed")
		continue
	return results

def create_output(case_num, results):
	ol = []
	for i in range(len(results)):
		ol.append("Case #{}: {}".format(i + 1, results[i]))
	return ol

def remove_empties(cases):
	while [] in cases:
		cases.remove([])
	return cases
	
#procedure
input_list = read_input(argv[1])
number_of_cases, cases = parse_input(input_list)
cases = remove_empties(cases)
case_results = determine_winners(cases)
output_list = create_output(number_of_cases, case_results)

for output in output_list:
	print output
