from sys import stdin
from itertools import product

def column(matrix, i):
	nRow = len(matrix)
	return [matrix[row][i] for row in range(nRow)]

def eliminate(lawn, N, M):
	mi = 101
	for i, j in product(range(N), range(M)):
		if lawn[i][j] < mi and lawn[i][j] > 0:
			mi = lawn[i][j]
			miInd = (i, j)

	#print mi
	#print miInd
	if mi == 101:
		return 1 # done lawn contains only 0

	valid = False

	rowSet = set()
	for e in lawn[miInd[0]]:
		rowSet.add(e)

	if (len(rowSet) == 1) or ((len(rowSet) == 2) and (0 in rowSet)):
		valid = True
		lawn[miInd[0]] = [0]*M

	if valid:
		return 0

	col = column(lawn, miInd[1])
	colSet = set()
	for e in col:
		colSet.add(e)

	if (len(colSet) == 1) or ((len(colSet) == 2) and (0 in colSet)):
		valid = True
		for r in range(N):
			lawn[r][miInd[1]] = 0

	if valid:
		return 0 # continue

	return -1


T = int(stdin.readline())

for case in range(1, T+1):
	N, M = map(int, stdin.readline().split())
	lawn = [None]*N

	for n in range(N):
		lawn[n] = map(int, stdin.readline().split())

	itr = 0
	while True:
		itr += 1
		#print "Iter: %d" % itr
		#print lawn

		result = eliminate(lawn, N, M)
		if result == 1:
			status = "YES"
			break
		elif result == -1:
			status = "NO"
			break
		

	print "Case #%d: %s" % (case, status)