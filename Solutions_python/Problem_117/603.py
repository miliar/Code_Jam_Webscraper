from sys import stdin

def parse2Darray(numRow):
	arr = [[] for i in range(numRow)]
	for i in range(numRow):
		arr[i] = [int(x) for x in stdin.readline().strip().split(' ')]
	return arr

T = int(stdin.readline())
for t in range(T):
	n, m = [int(x) for x in stdin.readline().strip().split(' ')]
	arr = parse2Darray(n)
	max_in_row = []
	max_in_col = []
	for i in range(n):
		max_in_row.append(max(arr[i]))
	for j in range(m):
		best = -1
		for i in range(n):
			if best < arr[i][j]:
				best = arr[i][j]
		max_in_col.append(best)
	can = 'YES'
	for i in range(n):
		for j in range(m):
			if (arr[i][j] != max_in_row[i] and arr[i][j] != max_in_col[j]):
				can = 'NO'
	print("Case #%d: %s" % (t + 1, can))
