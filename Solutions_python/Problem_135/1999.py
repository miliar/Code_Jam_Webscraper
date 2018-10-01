fileIn = open('x1.in', 'r')
fileOut = open('x1.out', 'w')

T = int(fileIn.readline().strip())

for case in range(1, T+1):
	rowNum1 = int(fileIn.readline().strip())

	grid = [[int(x) for x in fileIn.readline().strip().split()] for line in range(4)]
	row1 = grid[rowNum1 - 1]

	rowNum2 = int(fileIn.readline().strip())

	grid2 = [[int(x) for x in fileIn.readline().strip().split()] for _ in range(4)]
	row2 = grid2[rowNum2 - 1]

	union = []
	for num in row1:
		if num in row2:
			union.append(num)

	if len(union) == 1:
		fileOut.write("Case #{}: {}\n".format(case, union[0]))
	elif len(union) > 1:
		fileOut.write("Case #{}: Bad magician!\n".format(case))
	else:
		fileOut.write("Case #{}: Volunteer cheated!\n".format(case))