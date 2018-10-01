import sys;

n = input()

for ii in range(1, n + 1):
	dots = 0
	colX = [0, 0, 0, 0]
	colO = [0, 0, 0, 0]
	ldX, ldO, rdX, rdO = (0, 0, 0, 0)

	result = None
	
	for j in range(0, 4):
		rowX = 0
		rowO = 0

		row = raw_input()

		for i in range(0, 4):
			if row[i] == '.':
				dots += 1
			elif row[i] == 'O':
				rowO += 1
				colO[i] += 1
				if i == j: ldO += 1
				if i == 3 - j: rdO += 1
			elif row[i] == 'X':
				rowX += 1
				colX[i] += 1
				if i == j: ldX += 1
				if i == 3 - j: rdX += 1
			elif row[i] == 'T':
				colX[i] += 1
				colO[i] += 1
				rowX += 1
				rowO += 1
				if i == j: 
					ldO += 1
					ldX += 1
				if i == 3 - j:
					rdO += 1
					rdX += 1

		if rowX == 4:
			result = 'X won'
		elif rowO == 4:
			result = 'O won'

	blank = raw_input()

	for i in range(0, 4):
		if colX[i] == 4:
			result = 'X won'
		elif colO[i] == 4:
			result = 'O won'

	if result is None:
		if ldX == 4 or rdX == 4:
			result = 'X won'
		elif ldO == 4 or rdO == 4:
			result = 'O won'
		elif dots == 0:
			result = 'Draw'
		else:
			result = 'Game has not completed'

	print "Case #%s: %s" % (ii, result)
