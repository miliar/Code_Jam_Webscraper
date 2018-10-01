from sys import stdin
from itertools import product

def is_possible(lawn):
	rows = lawn
	columns = zip(*lawn)
	for r, c in product(range(len(rows)), range(len(columns))):
		height = lawn[r][c]
		if height != max(rows[r]) and height != max(columns[c]):
			return False
	return True

n = int(stdin.readline())
for i in range(1, n + 1):
	lawn = []
	height, width = map(int, stdin.readline().split(' '))
	for j in range(height):
		lawn.append(map(int, stdin.readline().split(' ')))
	message = 'YES' if is_possible(lawn) else 'NO'
	print 'Case #%d: %s' % (i, message)
