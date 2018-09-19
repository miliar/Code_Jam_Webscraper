#!/usr/bin/env python

def mark(M, H, W, R, label, y, x, dry_run=False):

	if not dry_run:
		label = mark(M, H, W, R, label, y, x, True)

	while 1:
		if not dry_run:
			R[y][x] = label

		altitude = M[y][x]
		diff = (0, 0)

		# North
		if y > 0 and M[y-1][x] < altitude:
			altitude = M[y-1][x]
			diff = (0, -1)
		# West
		if x > 0 and M[y][x-1] < altitude:
			altitude = M[y][x-1]
			diff = (-1, 0)
		# East
		if x+1 < W and M[y][x+1] < altitude:
			altitude = M[y][x+1]
			diff = (1, 0)
		# South
		if y+1 < H and M[y+1][x] < altitude:
			altitude = M[y+1][x]
			diff = (0, 1)

		if diff == (0, 0):
			break

		x += diff[0]
		y += diff[1]

		if R[y][x] is not None:
			break

	if R[y][x] is None:
		return 'a' if not label else chr(ord(label) + 1)
	else:
		return R[y][x]

def label_map(M, H, W):
	label = None
	R = [[None for col in xrange(W)] for row in xrange(H)]
	for row in xrange(H):
		for col in xrange(W):
			R[row][col] = None
	for row in xrange(H):
		for col in xrange(W):
			if R[row][col] is None:
				label = mark(M, H, W, R, label, row, col)
	return '\n'.join([' '.join(row) for row in R])

with open('in.txt') as fin:
	with open('out.txt', 'w') as fout:
		T = int(fin.readline().strip())
		for case in xrange(T):
			H, W = [int(i) for i in fin.readline().strip().split()]
			M = [[int(cell) for cell in fin.readline().strip().split()]
			     for i in xrange(H)]
			print >>fout, 'Case #%d:\n%s' % (case+1, label_map(M, H, W))
