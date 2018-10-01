import operator

def find_index_and_min(line):
	return min(enumerate(line), key=operator.itemgetter(1))

def find_lowest_square(lawn):
	min_ys = [find_index_and_min(line) for line in lawn]
	min_x, v = find_index_and_min([min_y[1] for min_y in min_ys])
	return min_x, min_ys[min_x][0], v

def load_lawn():
	n, m = [int(x) for x in raw_input().split()]
	lawn = []
	for i in range(0, n):
		lawn.append([int(x) for x in raw_input().split()])
	return n, m, lawn

def can_mow_horizontal(lawn, x, v):
	return lawn[x].count(v) == len(lawn[x])

def can_mow_vertical(lawn, y, v):
	yline = [line[y] for line in lawn]
	return yline.count(v) == len(yline)

def mow_horizontal(lawn, x):
	lawn.pop(x)
	return lawn

def mow_vertical(lawn, y):
	for line in lawn:
		line.pop(y)
	return lawn

def check_lawn(n, m, lawn):
	if n == 0 or m == 0:
		return 'YES'
	x, y, v = find_lowest_square(lawn)
	#print n, m, lawn, x, y, v
	if can_mow_horizontal(lawn, x, v):
		new_lawn = mow_horizontal(lawn, x)
		return check_lawn(n-1, m, new_lawn)
	elif can_mow_vertical(lawn, y, v):
		new_lawn = mow_vertical(lawn, y)
		return check_lawn(n, m-1, new_lawn)
	else:
		return 'NO'

k = int(raw_input())
for i in range(0, k):
	n, m, lawn = load_lawn()
	result = check_lawn(n, m, lawn)
	print 'Case #%s: %s' % (i+1, result)
