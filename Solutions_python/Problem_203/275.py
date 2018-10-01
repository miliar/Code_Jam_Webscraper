tc = int(input())

for cc in range(1, tc+1):
	r, c = [int(n) for n in input().split()]

	g = [['?' for x in range(c)] for y in range(r)]

	for y in range(r):
		lin = input()
		for x in range(c):
			ch = g[y][x] = lin[x]

	for y in range(r):
		for x in range(1, c):
			if g[y][x] == '?':
				g[y][x] = g[y][x-1]
		for x in range(c-2, -1, -1):
			if g[y][x] == '?':
				g[y][x] = g[y][x+1]

	for y in range(1,r):
		if g[y].count('?') == c:
			g[y] = g[y-1]

	for y in range(r-2, -1, -1):
		if g[y].count('?') == c:
			g[y] = g[y+1]

	print("Case #{}:".format(cc))

	for y in range(r):
		print(''.join(g[y]))

