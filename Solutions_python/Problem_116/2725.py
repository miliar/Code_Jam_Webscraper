
fout = open('A-small-attempt1.out', 'w')
fin = open('A-small-attempt1.in', 'r')
first_line = fin.readline().strip('\r\n')

for i in range(int(first_line)):
	line1 = fin.readline().strip('\r\n')
	line2 = fin.readline().strip('\r\n')
	line3 = fin.readline().strip('\r\n')
	line4 = fin.readline().strip('\r\n')
	fin.readline()

	line = [line1, line2, line3, line4]
	
	is_dot_present = False
	pivot = line[0][0]
	if pivot != '.' and (line[0][0] == pivot or line[0][0] == 'T') and \
		(line[1][1] == pivot or line[1][1] == 'T') and \
		(line[2][2] == pivot or line[2][2] == 'T') and \
		(line[3][3] == pivot or line[3][3] == 'T'):
		fout.write("Case #%i: %s won\n" %(i+1, pivot))
		continue

	pivot = line[0][3]
	if pivot != '.' and (line[0][3] == pivot or line[0][3] == 'T') and \
		(line[1][2] == pivot or line[1][2] == 'T') and \
		(line[2][1] == pivot or line[2][1] == 'T') and \
		(line[3][0] == pivot or line[3][0] == 'T'):
		fout.write("Case #%i: %s won\n" %(i+1, pivot))
		continue

	found_winner = False
	for j in range(4):
		count = 1
		if found_winner:
			break
		
		pivot = line[j][0]

		for k in range(4):
			if line[j][k] == '.':
				is_dot_present = True
				found_winner = False
				break

			if line[j][k] == pivot or line[j][k] == 'T':
				count = count + 1
				
				if count == 4:
					found_winner = True
			else:
				found_winner = False
				break

	if found_winner:
		fout.write("Case #%i: %s won\n" %(i+1, pivot))
		continue
	else:
		for j in range(4):
			count = 1
			if found_winner:
				break

			pivot = line[0][j]

			for k in range(4):
				if line[k][j] == '.':
					is_dot_present = True
					found_winner = False
					break

				if line[k][j] == pivot or line[k][j] == 'T':
					count = count + 1
					if count == 4:
						found_winner = True
				else:
					found_winner = False
					break	

	if found_winner:
		fout.write("Case #%i: %s won\n" %(i+1, pivot))
	elif is_dot_present:
		fout.write("Case #%i: Game has not completed\n" %(i+1))
	else:
		fout.write("Case #%i: Draw\n" %(i+1))
	
fout.close()
fin.close()