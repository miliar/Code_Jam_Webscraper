import sys

n = int(sys.stdin.readline())

def xs(s):
	return s in {'XXXT', 'XXTX', 'XTXX', 'TXXX', 'XXXX'}

def os(s):
	return s in {'OOOT', 'OOTO', 'OTOO', 'TOOO', 'OOOO'}

def f(a):
	for i in xrange(4):
		s = a[i]
		if xs(s): return 'X won'
		if os(s): return 'O won'
		s = a[0][i] + a[1][i] + a[2][i] + a[3][i]
		if xs(s): return 'X won'
		if os(s): return 'O won'
	s = a[0][0] + a[1][1] + a[2][2] + a[3][3]
	if xs(s): return 'X won'
	if os(s): return 'O won'
	s = a[0][3] + a[1][2] + a[2][1] + a[3][0]
	if xs(s): return 'X won'
	if os(s): return 'O won'
	if '.' in ''.join(a):
		return 'Game has not completed'
	return 'Draw'


for t in xrange(n):
	a = []
	for _ in xrange(4):
		a.append(sys.stdin.readline().strip())
	sys.stdin.readline()
	print 'Case #%d:' % (t+1), f(a)


