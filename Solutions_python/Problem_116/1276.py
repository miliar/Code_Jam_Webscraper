def input(fin):
	arr = []
	for i in range(4):
		arr.append(fin.readline())

	fin.readline()
	return arr

def process(arr):
	d = True
	for i in range(4):
		tx = 0
		to = 0
		for j in range(4):
			if arr[i][j] == 'X' or arr[i][j] == 'T':
				tx = tx + 1
			if arr[i][j] == 'O' or arr[i][j] == 'T':
				to = to + 1
			if arr[i][j] == '.':
				d = False
		if tx == 4:
			return 'X won'
		if to == 4:
			return 'O won'

		tx = 0
		to = 0
		for j in range(4):
			if arr[j][i] == 'X' or arr[j][i] == 'T':
				tx = tx + 1
			if arr[j][i] == 'O' or arr[j][i] == 'T':
				to = to + 1
		if tx == 4:
			return 'X won'
		if to == 4:
			return 'O won'

	tx = 0
	to = 0
	for i in range(4):
		if arr[i][i] == 'X' or arr[i][i] == 'T':
			tx = tx + 1
		if arr[i][i] == 'O' or arr[i][i] == 'T':
			to = to + 1
	if tx == 4:
		return 'X won'
	if to == 4:
		return 'O won'
	tx = 0
	to = 0
	for i in range(4):
		if arr[i][3 - i] == 'X' or arr[i][3 - i] == 'T':
			tx = tx + 1
		if arr[i][3 - i] == 'O' or arr[i][3 - i] == 'T':
			to = to + 1
	if tx == 4:
		return 'X won'
	if to == 4:
		return 'O won'

	if d:
		return 'Draw'
	else:
		return 'Game has not completed'

def output(fout, res):
	print res
	fout.write(res + '\n')

fin = open('1.in')
fout = open('1.out', 'w')
t = int(fin.readline())
for i in range(t):
	output(fout, 'Case #%d: ' % (i + 1) + process(input(fin)))