def magic(file_name):
	file_data = open(file_name, 'r')
	n = int(file_data.readline())
	print n
	for i in range(n):
		row1 = int(file_data.readline())
		row_data1 = []
		for j in range(4):
			row_data1.append(file_data.readline().strip('\n').split(' '))
		# print row_data1[row1 - 1]
		row2 = int(file_data.readline())
		row_data2 = []
		for j in range(4):
			row_data2.append(file_data.readline().strip('\n').split(' '))
		# print row_data2[row2 - 1]
		guess = set(row_data1[row1 - 1]).intersection(set(row_data2[row2 - 1]))
		# print row
		print "Case #" + str(i + 1) + ":",
		if len(guess) == 1:
			print list(guess)[0]
		elif len(guess) > 1:
			print "Bad magician!"
		elif len(guess) == 0:
			print "Volunteer cheated!"


magic('input.in')