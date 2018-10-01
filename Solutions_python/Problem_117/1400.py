f = open('B-large.in')

numbers_input = f.readline().split(' ')
T = int(numbers_input[0])

for i in range(T):
	N, M = (int(j) for j in f.readline().split(' '))
	pole = []
	row_max = []
	col_max = []
	
	for k in range(N):
		pole.append([int(j) for j in f.readline().rstrip().split()])
		row_max.append(max(pole[k]))

	for k in range(M):
		col_max.append(max([j[k] for j in pole]))
	
	flag = False
	for row in range(N):
		for col in range(M):
			if pole[row][col] < row_max[row] and pole[row][col] < col_max[col]:
				flag = True
				break
		if flag:
			print('Case #%d: NO' % (i+1))
			break
	else:
		print('Case #%d: YES' % (i+1))