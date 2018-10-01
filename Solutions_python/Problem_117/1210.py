def tic():
	f = open("/home/jackiebaek/codejam/test.in")
	times = -1
	lines = f.readlines()

	cases = int(lines.pop(0))
	for i in range(cases):
		header = lines.pop(0).split()
		num_lines = int(header[0])
		num_columns = int(header[1])

		grid = []
		for j in range(num_lines):
			grid.append([int(s) for s in lines.pop(0).split()])

		#print grid
		print "Case #%i:" % (i+1),
		determinePossible(grid, num_lines, num_columns)

def determinePossible(grid, rows, columns):
	row_max = []
	col_max = []
	for row in grid:
		row_max.append(max(row))
	for i in range(columns):
		column = [grid[j][i] for j in xrange(rows)]
		col_max.append(max(column))
	#print row_max, col_max
	# now row_max, col_max has all the maximums

	for i in range(rows):
		for j in range(columns):
			square = grid[i][j]
			if square < row_max[i] and square < col_max[j]:
				print "NO"
				return
	print "YES"

tic()