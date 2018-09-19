def at_line(string_list):
	winner = ""
	for ind in range(len(string_list)):
		x, o = 0, 0
		for string in string_list[ind]:
			if string == "X" or string == "T":
				x += 1
			if string == "O" or string == "T":
				o += 1
		if x == 4:
			winner = "X"
		elif o == 4:
			winner = "O"
	return winner
	
def at_column(string_list):
	winner = ""
	for i in range(len(string_list)):
		x, o = 0, 0
		for j in range(len(string_list[i])):
			if string_list[j][i] == "X" or string_list[j][i] == "T":
				x += 1
			if string_list[j][i] == "O" or string_list[j][i] == "T":
				o += 1 
		if x == 4:
			winner = "X"
		elif o == 4:
			winner = "O"
	return winner
	
def first_diagonal(string_list):
	winner = ""
	x, o = 0, 0
	for i in range(len(string_list)):
		for j in range(len(string_list[i])):
			if i == j:
				if string_list[j][i] == "X" or string_list[j][i] == "T":
					x += 1
				if string_list[j][i] == "O" or string_list[j][i] == "T":
					o += 1 
	if x == 4:
		winner = "X"
	elif o == 4:
		winner = "O"
	return winner

def second_diagonal(string_list):
	winner = ""
	x, o = 0, 0
	for i in range(len(string_list)):
		for j in range(len(string_list[i])):
			if i + j == 3:
				if string_list[i][j] == "X" or string_list[i][j] == "T":
					x += 1
				if string_list[i][j] == "O" or string_list[i][j] == "T":
					o += 1 
	if x == 4:
		winner = "X"
	elif o == 4:
		winner = "O"
	return winner

def is_complete(string_list):
	count = ""
	for i in range(len(string_list)):
		for string in string_list[i]:
			if string == ".":
				count += string
	if count:
		return False
	else:
		return True

def print_results(list_of_lists):
	for i in range(len(list_of_lists)):
		complete = False
		result = str(at_line(list_of_lists[i])) + str(at_column(list_of_lists[i])) + str(first_diagonal(list_of_lists[i])) + str(second_diagonal(list_of_lists[i]))
		if not result:
			if is_complete(list_of_lists[i]):
				result = "Draw"
			else:
				result = "Game has not completed"
		else:
			result = result[0] + " won"
		print "Case #" + str(i + 1) + ": " + result
						
n = int(raw_input())
big_list = []
while n > 0:
	list = []
	for i in range(4):
		line = raw_input()
		list.append(line)
	empty = raw_input()
	big_list.append(list)
	n -= 1

print_results(big_list)
		
	
				
				
