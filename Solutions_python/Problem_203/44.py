import sys

pin = sys.stdin
pout = sys.stdout

def solve():
	n, m = [int(x) for x in pin.readline().split()]
	# print(n, m)
	line = []
	for i in range(n):
		line.append([x for x in pin.readline()])
		# print(line[i])
	for i in range(1, n):
		for j in range(m):
			if line[i][j] == '?': line[i][j] = line[i-1][j]
	for i in range(n-2, -1, -1):
		# print(i)
		for j in range(m):
			if line[i][j] == '?': line[i][j] = line[i+1][j]
	for i in range(n):
		for j in range(1, m):
			if line[i][j] == '?': line[i][j] = line[i][j-1]
	for i in range(n):
		for j in range(m-2, -1, -1):
			if line[i][j] == '?': line[i][j] = line[i][j+1]
	for i in range(n):
		print(''.join(line[i][:-1]))


nq = int(pin.readline())
for q in range(1, nq+1):
	print("Case #%d:"%q)
	solve();
