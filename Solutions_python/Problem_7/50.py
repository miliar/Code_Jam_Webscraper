# coding: utf8
# rozwiązanie ?
import sys


#def triangles(n, A, B, )


if len(sys.argv) > 1:
	f_name = sys.argv[1]
else:
	f_name = "A.in"

fh = open(f_name)
N = int(fh.readline())

def to_xy(n):
	return n / 3, n % 3

def ok_ijk(i, j, k):
	xi, yi = to_xy(i)
	xj, yj = to_xy(j)
	xk, yk = to_xy(k)
	return (xi + xj + xk) % 3 == 0 and (yi + yj + yk) % 3 == 0

def triangles(t, i, j, k):
	xi, yi = to_xy(i)
	xj, yj = to_xy(j)
	xk, yk = to_xy(k)

	ni = t[xi][yi]
	nj = t[xj][yj]
	nk = t[xk][yk]
	if i == j == k:
		return ni * (nj-1) * (nk-2) / 6
	if i == j:
		return ni * (nj-1) * nk / 2
	if i == k:
		return ni * nj * (nk-1) / 2
	if j == k:
		return ni * nj * (nk-1) / 2
	return ni * nj * nk

for c in xrange(N):
	n, A, B, C, D, x, y, M = [int(x) for x in fh.readline().split()]
#	print n, A, B, C, D, x, y, M
	t = [[0]*3,[0]*3, [0]*3]

	t[x % 3][y % 3] += 1
	for i in xrange(n-1):
		x = (A * x + B) % M
		y = (C * y + D) % M
		t[x % 3][y % 3] += 1

#	print t

	S = 0
	visited = dict()
	for i in xrange(9):
		for j in xrange(9):
			for k in xrange(9):
				if not ok_ijk(i, j, k):
					continue
				v = tuple(sorted([i, j, k]))
				if v in visited:
					continue
				visited[v] = 1
				S += triangles(t, i, j, k)
	print "Case #%d: %d" % (c+1, S)

