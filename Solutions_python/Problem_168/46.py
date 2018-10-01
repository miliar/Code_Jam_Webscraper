def solve():
	r, c = (int(x) for x in input().split())
	field = [input() for i in range(r)]
	impossible = [[0] * c for _ in range(r)]
	change = [[0] * c for _ in range(r)]
	for i in range(r):
		for j in range(c):
			if field[i][j] != '.':
				impossible[i][j] += 1
				if field[i][j] == '<':
					change[i][j] = 1
				break
		for j in range(c - 1, -1, -1):
			if field[i][j] != '.':
				impossible[i][j] += 1
				if field[i][j] == '>':
					change[i][j] = 1
				break
	for i in range(c):
		for j in range(r):
			if field[j][i] != '.':
				impossible[j][i] += 1
				if field[j][i] == '^':
					change[j][i] = 1
				break
		for j in range(r - 1, -1, -1):
			if field[j][i] != '.':
				impossible[j][i] += 1
				if field[j][i] == 'v':
					change[j][i] = 1
				break
	ans = 0
	for ri, rc in zip(impossible, change):
		for x, y in zip(ri, rc):
			if y:
				if x == 4:
					return 'IMPOSSIBLE'
				ans += 1
	return ans

t = int(input())
for i in range(t):
	print('Case #{}: {}'.format(i + 1, solve()))
