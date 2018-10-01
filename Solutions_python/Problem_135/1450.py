num_of_cases = int(raw_input())

for x in range (1,num_of_cases  + 1):
	first_row_index = int(raw_input())
	for y in range (1,5):
		if y == first_row_index:
			first_row  = raw_input().split()
		else:
			raw_input()
	second_row_index = int(raw_input())
	for y in range (1,5):
		if y == second_row_index:
			second_row  = raw_input().split()
		else:
			raw_input()
	conflicts = []
	for num1 in  first_row:
		for num2 in second_row:
			if num1 == num2 and num1 not in conflicts:
				conflicts.append(num1)
	if len(conflicts) > 1:
		out_str = 'Bad Magician!'
	elif len(conflicts) == 1:
		out_str = conflicts[0]
	else:
		out_str = 'Volunteer cheated!'
	print "Case #%d: %s" % (x,out_str)