import sys 
def read_matrix():
	numbers = []
	i = 0;
	while i < 4:
		numbers.append(raw_input().split(' '))
		i += 1
	return numbers

def get_selected_row():
	rownum = input()
	matrix = read_matrix()
	required_row = matrix[rownum - 1]	
	return required_row	
	
def get_intersection(row1, row2):
	values = []
	i = 0
	j = 0
	while i < len(row1):
		if row1[i] in row2:
			values.append(row1[i])
			j += 1
		i += 1
	return values

def identify_type(common_values):
	if len(common_values) > 1:
		print "Bad magician!"
	elif len(common_values) == 0:
		print "Volunteer cheated!"
	else:
		print common_values[0]

def main():
	i = 0
	t = input()
	while i < t:
		i += 1
		row1 = get_selected_row()
		row2 = get_selected_row()
		common_values = get_intersection(row1, row2)
		
		sys.stdout.write("Case #" + str(i) + ": ")
		identify_type(common_values)
		
main()		   

