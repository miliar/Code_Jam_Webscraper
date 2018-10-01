import sys

input_list = []
output_list = []

def work(input_line):
#	print input_line
	result = ''
	#X wins?
	for x in [0, 1, 2, 3]:
		col_count = 0
		for y in [0, 1, 2, 3]:
			if input_line[x][y] == 'O' or input_line[x][y] == '.':
				pass
			else:
				col_count += 1
		if col_count == 4:
			result = 'X won'
			return result
	for y in [0, 1, 2, 3]:
		row_count = 0
		for x in [0, 1, 2, 3]:
			if input_line[x][y] == 'O' or input_line[x][y] == '.':
				pass
			else:
				row_count += 1
		if row_count == 4:
			result = 'X won'
			return result
	dia_count = 0
	for x in [0, 1, 2, 3]:
		if input_line[x][x] == 'O' or input_line[x][x] == '.':
			pass
		else:
			dia_count += 1
	if dia_count == 4:
		result = 'X won'
		return result
	dia_count = 0
	for x in [0, 1, 2, 3]:
		if input_line[x][3-x] == 'O' or input_line[x][3-x] == '.':
			pass
		else:
			dia_count += 1
	if dia_count == 4:
		result = 'X won'
		return result
	
	# O win?
	for x in [0, 1, 2, 3]:
		col_count = 0
		for y in [0, 1, 2, 3]:
			if input_line[x][y] == 'X' or input_line[x][y] == '.':
				pass
			else:
				col_count += 1
		if col_count == 4:
			result = 'O won'
			return result
	for y in [0, 1, 2, 3]:
		row_count = 0
		for x in [0, 1, 2, 3]:
			if input_line[x][y] == 'X' or input_line[x][y] == '.':
				pass
			else:
				row_count += 1
		if row_count == 4:
			result = 'O won'
			return result
	dia_count = 0
	for x in [0, 1, 2, 3]:
		if input_line[x][x] == 'X' or input_line[x][x] == '.':
			pass
		else:
			dia_count += 1
	if dia_count == 4:
		result = 'O won'
		return result
	dia_count = 0
	for x in [0, 1, 2, 3]:
		if input_line[x][3-x] == 'X' or input_line[x][3-x] == '.':
			pass
		else:
			dia_count += 1
	if dia_count == 4:
		result = 'O won'
		return result

	# else:
	dot_count = 0
	for x in [0, 1, 2, 3]:
		for y in [0, 1, 2, 3]:
			if input_line[x][y] == '.':
				dot_count += 1
	if dot_count > 0:
		result = 'Game has not completed'
		return result

	result = 'Draw'
	return result

try:
	input_filename = sys.argv[1]
	output_filename = input_filename[:sys.argv[1].find('.')]+'.out'
except:
	print 'input filename as argv'
	exit()

try:
	input_f = open("./"+input_filename)
	input_lines = input_f.readlines()
	input_line_list = []
	input_count = 0
	for input_line in input_lines:
		input_count += 1
		input_line_list.append(input_line[:4])
		if input_count == 5:
			input_list.append(input_line_list)
			input_line_list = []
			input_count = 0
#		input_split = input_line.split()
#		input_list.append(input_split)
	input_f.close()
except:
	print 'read error'
	exit()
print input_list

for input_line in input_list:

	input_line.pop(0)
	# do some works here
	if len(input_line) != 4:
		print input_line
		pass
	else:
		result = work(input_line)
		output_list.append([result])

try:
	output_f = open("./"+output_filename, "w")
	output_f.close()
except:
	pass

try:
	output_f = open("./"+output_filename, "a")
	output_str = ''

	for x in range(len(output_list)):
		output_f.write('Case #' + str(x+1)+': '+str(output_list[x][0])+"\n")
		print x
	output_f.close()
except:
	print 'write error'
	exit()
