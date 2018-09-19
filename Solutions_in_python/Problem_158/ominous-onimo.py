f = open('D-small-attempt1.in.txt', 'r')

T = 0

i = 0
for line in f:
	if (i == 0):
		T = int(line)
	else:
		split = line.split()
		ints = map(int,split)
		X = ints[0]
		R = ints[1]
		C = ints[2]
		winner = ''
		possible = False # possible for Gabriel to complete puzzle using Richard's optimal choice
		area = R * C
		if (X == 1):
			possible = True
		elif (X == 2):
			if (area == 1 or area == 3 or area == 9):
				possible = False
			else:
				possible = True
		elif (X == 3):
			if (area == 6 or area == 9 or area == 12):
				possible = True
			else:
				possible = False
		elif (X == 4):
			if (area == 12 or area == 16):
				possible = True
			else:
				possible = False

		if (possible):
			winner = 'GABRIEL'
		else:
			winner = 'RICHARD'

		print('Case #' + str(i) + ': ' + str(winner))
	i += 1



f.close()