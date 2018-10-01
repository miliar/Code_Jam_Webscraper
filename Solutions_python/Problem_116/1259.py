from sys import stdin, stdout

lines = list(map(lambda l : l[:-1], stdin.readlines()))

t = int(lines[0])

def solve(f):
	# print("-----")
	# for l in field:
	# 	print(l)
	# print("-----")

	def wins(c1, c2, c3, c4, p):
		# print(c1)
		# print(c2)
		# print(c3)
		# print(c4)
		return (c1 == p or c1 == 'T') and (c2 == p or c2 == 'T') and (c3 == p or c3 == 'T') and (c4 == p or c4 == 'T')

	filled = True

	wx = False
	wo = False
	for i in range(4):
		for j in range(4):
			if f[i][j] == '.':
				filled = False

	for j in range(4):
		c1 = f[0][j]
		c2 = f[1][j]
		c3 = f[2][j]
		c4 = f[3][j]
		if wins(c1, c2, c3, c4, 'X'):
			wx = True
		if wins(c1, c2, c3, c4, 'O'):
			wo = True
			
	for i in range(4):
		c1 = f[i][0]
		c2 = f[i][1]
		c3 = f[i][2]
		c4 = f[i][3]
		if wins(c1, c2, c3, c4, 'X'):
			wx = True
		if wins(c1, c2, c3, c4, 'O'):
			wo = True

	c1 = f[0][0]
	c2 = f[1][1]
	c3 = f[2][2]
	c4 = f[3][3]
	if wins(c1, c2, c3, c4, 'X'):
		wx = True
	if wins(c1, c2, c3, c4, 'O'):
		wo = True

	c1 = f[0][3]
	c2 = f[1][2]
	c3 = f[2][1]
	c4 = f[3][0]
	if wins(c1, c2, c3, c4, 'X'):
		wx = True
	if wins(c1, c2, c3, c4, 'O'):
		wo = True

	return wx, wo, filled


cur = 1
for test in range(t):
	field = [lines[cur], lines[cur + 1], lines[cur + 2], lines[cur + 3]]
	cur += 5
	wx, wo, filled = solve(field)
	ress = None
	if wx:
		ress = "X won"
	elif wo:
		ress = "O won"
	elif filled:
		ress = "Draw"
	else:
		ress = "Game has not completed"
	print("Case #{}: {}".format(test + 1, ress))


# print(lines[1:])