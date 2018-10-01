

import re
import sys

in_file = sys.argv[1]
print in_file

input_file = open(in_file, 'rb')
output_file = open(in_file+'_output.txt', 'w+')

num_cases = int(input_file.next())
cases = []

def win(line, char):
	if 'T' in line and line.count(char) == 3:
		return True
	elif line.count(char) == 4:
		return True

def x_won(rows):
	#check rows
	for row in rows:
		if win(row, 'X'):
			return True
	#check cols
	for i in range(0, 4):
		col = []
		for row in rows:
			col.append(row[i])
		if win(col, 'X'):
			return True
	#check diagonals
	diag_1 = []
	diag_1.append(rows[0][0])
	diag_1.append(rows[1][1])
	diag_1.append(rows[2][2])
	diag_1.append(rows[3][3])

	diag_2 = []
	diag_2.append(rows[3][0])
	diag_2.append(rows[2][1])
	diag_2.append(rows[1][2])
	diag_2.append(rows[0][3])

	if win(diag_1, 'X'):
		return True
	if win(diag_2, 'X'):
		return True

	return False

def o_won(rows):
	#check rows
	for row in rows:
		if win(row, 'O'):
			return True
	#check cols
	for i in range(0, 4):
		col = []
		for row in rows:
			col.append(row[i])
		if win(col, 'O'):
			return True
	#check diagonals
	diag_1 = []
	diag_1.append(rows[0][0])
	diag_1.append(rows[1][1])
	diag_1.append(rows[2][2])
	diag_1.append(rows[3][3])

	diag_2 = []
	diag_2.append(rows[3][0])
	diag_2.append(rows[2][1])
	diag_2.append(rows[1][2])
	diag_2.append(rows[0][3])

	if win(diag_1, 'O'):
		return True
	if win(diag_2, 'O'):
		return True

	return False

def draw(rows):
	for row in rows:
		if '.' in row:
			return False
	return True



for i in range(num_cases):
	rows = []
	for j in range(0, 4):
		line = input_file.next()
		row = []
		row.append(line[0])
		row.append(line[1])
		row.append(line[2])
		row.append(line[3])
		rows.append(row)
	if x_won(rows):
		cases.append("X won")
	elif o_won(rows):
		cases.append("O won")
	elif draw(rows):
		cases.append("Draw")
	else:
		cases.append("Game has not completed")
	print (cases[i])
	try:
		line = input_file.next() #throw away a spacing line
	except StopIteration:
		break


for i, result in enumerate(cases):
	output_file.write("Case #%d: %s" % (i+1, result) + "\n")