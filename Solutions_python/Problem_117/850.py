f = open('lawnmower.in')
out = open('lawnmower.out', 'w')
cases = int(f.readline())

def mowable(grid, length, width):
	for height in range(1, 100+1):
		# check row
		for row in range(length):
			result = array_full(grid[row], height)
			if result is None:
				return False
			if result:
				grid[row] = [-1] * width

		# check col
		for col in range(width):
			arr = [grid[x][col] for x in range(length)]
			result = array_full(arr, height)
			if result is None:
				return False
			if result:
				for i in range(length):
					grid[i][col] = -1

	return True

def array_full(arr, val):
	for i in arr:
		if i == -1 or i == val:
			continue
		elif i > val:
			return False
		elif i < val:
			return None
	return True

for case in range(1, cases+1):
	line = f.readline().split()
	length, width = int(line[0]), int(line[1])

	grid = []
	for _ in range(length):
		grid.append(map(lambda x: int(x), f.readline().split()))

	answer = "YES" if mowable(grid, length, width) else "NO"
	out.write("Case #{0}: {1}\n".format(case, answer))
