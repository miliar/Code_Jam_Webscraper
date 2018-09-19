file = open('A-small-attempt5.in', 'r')
file_out = open('output.txt', 'w')
test_cases = int(file.readline())
print 'Test Cases ', test_cases
initial_matrix = []
temp_row = []
final_matrix = []
possible_answers = []
count = 0
line = file.readline()
for test_case in range (1, test_cases + 1):
	count += 1
	initial_row = int(line)
	for row in range(0,4):
		line = file.readline()
		for num in line.split():
			temp_row.append(int(num))
		initial_matrix.append(temp_row)
		temp_row = []
	final_row = int(file.readline())
	for row in range(0,4):
		line = file.readline()
		for num in line.split():
			temp_row.append(int(num))
		final_matrix.append(temp_row)
		temp_row = []
	for i in initial_matrix[initial_row - 1]:
		for j in final_matrix[final_row - 1]:
			if( i == j):
				possible_answers.append(i)			
	if len(possible_answers) == 1:
		output = 'Case #' + str(test_case) +': ' + str(possible_answers[0])
	elif len(possible_answers) == 0:
		output= 'Case #' + str(test_case) + ': Volunteer Cheated!'
	else:
		output = 'Case #' + str(test_case) + ': Bad Magician!'
	file_out.write(output)
	file_out.write('\n')
	possible_answers = []
	line = file.readline()
	initial_matrix = []
	final_matrix = []

file_out.close()
file.close()
