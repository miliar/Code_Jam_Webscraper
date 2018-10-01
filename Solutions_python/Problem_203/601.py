file1 = open('C:/Users/dxsun/Desktop/Coding/Google Code Jam 2017/Round 1/cake_input_large.in','r')
file2 = open('C:/Users/dxsun/Desktop/Coding/Google Code Jam 2017/Round 1/cake_output_large.txt','w')


def fill(row, i, char, start=0):
	for x in range(start, i):
		row[x] = char

cases = file1.readline()
counter = 0
for line in file1:
	counter += 1
	r, c = line.split()
	r = int(r)
	c = int(c)
	grid = []
	for i in range(r):
		temp = [char for char in file1.readline()]
		if temp[-1] == "\n":
			temp.pop(-1)
		grid.append(temp)
	# print(grid)

	start_row = 0
	stop = False
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] != '?':
				start_row = i
				stop = True
				break
		if stop:
			break

	for i in range(start_row, len(grid)):
		indices = []
		row = grid[i]
		for j in range(len(grid[0])):
			if row[j] != '?':
				indices.append(j)
		if len(indices) == 0:
			grid[i] = grid[i-1].copy()
		elif len(indices) == 1:
			fill(row, c, row[indices[0]])
		#if multiple indices with letters
		else:
			for pos in range(len(indices)-1):
				if pos == 0:
					fill(row, indices[0], row[indices[0]])
				else:
					# print(pos)
					# print(indices)
					# print(row)
					# print(i)
					fill(row, indices[pos], row[indices[pos]], indices[pos-1]+ 1)
			fill(row, c, row[indices[-1]], indices[-2] + 1)

	if start_row > 0:
		for row in range(start_row):
			grid[row] = grid[start_row]

	file2.write("Case #" + str(counter) + ":\n")
	for row in grid:
		file2.write(''.join(row) + "\n")
	# print("LMOA")

file1.close()
file2.close()
