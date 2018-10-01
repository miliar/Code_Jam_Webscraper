f = open('A-small-attempt2.in')

numbers_input = f.readline().split(' ')
T = int(numbers_input[0])

i = 1
while i <= T:
	have_point = False
	pole = []
	pole.append(f.readline().rstrip())
	pole.append(f.readline().rstrip())
	pole.append(f.readline().rstrip())
	pole.append(f.readline().rstrip())
	f.readline()
	
	diag1 = [pole[0][0], pole[1][1], pole[2][2], pole[3][3]]
	diag2 = [pole[0][3], pole[1][2], pole[2][1], pole[3][0]]
	
	if (diag1.count('X') + diag1.count('T'))==4 or (diag2.count('X') + diag2.count('T'))==4:
		print('Case #%d: X won' % i)
		i += 1
		continue
	elif (diag1.count('O') + diag1.count('T'))==4 or (diag2.count('O') + diag2.count('T'))==4:
		print('Case #%d: O won' % i)
		i += 1
		continue
	
	j = 0
	while j < 4:
		if pole[j][j] == 'X' or pole[j][j] == 'T':
			if (pole[j].count('X') + pole[j].count('T'))==4:
				print('Case #%d: X won' % i)
				break
			else:
				col_p = [pole[0][j], pole[1][j], pole[2][j], pole[3][j]]
				if (col_p.count('X') + col_p.count('T'))==4:
					print('Case #%d: X won' % i)
					break
		elif pole[j][j] == 'O' or pole[j][j] == 'T':
			if (pole[j].count('O') + pole[j].count('T'))==4:
				print('Case #%d: O won' % i)
				break
			else:
				col_p = [pole[0][j], pole[1][j], pole[2][j], pole[3][j]]
				if (col_p.count('O') + col_p.count('T'))==4:
					print('Case #%d: O won' % i)
					break
		if (have_point == False) and (pole[j].count('.') != 0):
			have_point = True
		j += 1
	else:
		if have_point:
			print('Case #%d: Game has not completed' % i)
		else:
			print('Case #%d: Draw' % i)
	i += 1