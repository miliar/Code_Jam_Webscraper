import sys

f = open('small.in', 'r')
g = open('small.out', 'w')

T = int(f.readline())
test_num = 0

def main():
	global test_num
	
	for sets in range(T):
		test_num = sets + 1
		size_params = str.strip(f.readline()).split(' ')
		N = int(size_params[0])
		M = int(size_params[1])
		
		board_h = []
		board_v = []
		board_compare = []
		row_max_val = []
		column_max_val = []
		
		# Fill board_h and board_compare
		for row in range(N):
			current_row = str.strip(f.readline()).split(' ')
			compare_row = []
			for column in range(M):
				current_row[column] = int(current_row[column])
				compare_row.append(100)
				
			board_h.append(current_row)
			board_compare.append(compare_row)
		
		# Fill board_v
		for column in range(len(board_h[0])):
			current_column = []
			for row in range(len(board_h)):
				current_column.append(board_h[row][column])
			board_v.append(current_column)
			
		# Find row max
		for row in board_h:
			temp_max = -1
			for column in row:
				if temp_max <= column:
					temp_max = column
					
			row_max_val.append(temp_max)
		
		# Find column max
		for column in board_v:
			temp_max = -1
			for row in column:
				if temp_max <= row:
					temp_max = row
					
			column_max_val.append(temp_max)
		
		# Mow board_compare rows
		for row in range(len(board_compare)):
			for column in range(len(board_compare[row])):
				if board_compare[row][column] > row_max_val[row]:
					board_compare[row][column] = row_max_val[row]
					
		# Mow board_compare columns
		for column in range(len(board_compare[0])):
			for row in range(len(board_compare)):
				if board_compare[row][column] > column_max_val[column]:
					board_compare[row][column] = column_max_val[column]
		
		# Compare board_compare to input
		compare_fail = False
		for row in range(len(board_h)):
			for column in range(len(board_h[row])):
				if board_h[row][column] != board_compare[row][column]:
					compare_fail = True
					print_result(False)
					break
			if compare_fail == True:
				break
					
		if compare_fail == False:
			print_result(True)
		
	f.close()
	g.close()
	sys.exit()

	

def print_result(possible):
	if possible == True:
		g.write("Case #" + str(test_num) + ": YES\n")
	else:
		g.write("Case #" + str(test_num) + ": NO\n")
	return
	
	
main()