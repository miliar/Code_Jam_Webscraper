import sys

input = [map(int, line.split()) for line in sys.stdin]
s = 1
for t in xrange(input[0][0]):
	h = input[s][0]
	w = input[s][1]
	m = input[s+1:s+h+1]
	s += h+1
	maxrow = map(max, m)
	maxcol = map(max, zip(*m))
	bad = 0
	for i in xrange(h):
		for j in xrange(w):
			if m[i][j] != maxrow[i] and m[i][j] != maxcol[j]:
				bad = 1
	print "Case #{0}: ".format(t+1),
	if bad:
		print "NO"
	else:
		print "YES"
