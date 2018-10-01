from math import *

filename = 'A-large'
fin = open('%s.in' % filename)
fout = open('%s.out' % filename, 'w')

cases = int(fin.readline().strip())
for case in xrange(cases):
	n = int(fin.readline().strip())
	g = []
	WP = [0] * n
	OWP = [0] * n
	OOWP = [0] * n
	WPn = []
	for i in xrange(n):
		WPn.append([0] * n)
		g.append(fin.readline().strip())
		w = 0
		m = 0
		for j in g[i]:
			if (j != '.'):
				m += 1
			if (j == '1'):
				w += 1
		WP[i] = 1.0 * w / m
		for j in xrange(n):
			if (g[i][j] == '.'):
				WPn[i][j] = WP[i]
			else:
				WPn[i][j] = 1.0 * (w-int(g[i][j])) / (m-1)
	for i in xrange(n):
		w = 0
		m = 0
		for j in xrange(n):
			if (i != j and g[i][j] != '.'):
				w += WPn[j][i]
				m += 1
		OWP[i] = w / m
	for i in xrange(n):
		w = 0
		m = 0
		for j in xrange(n):
			if (i != j and g[i][j] != '.'):
				w += OWP[j]
				m += 1
		OOWP[i] = w / m
	RPI = [0] * n
	print 'Case #%d:\n' % (case+1), 
	for i in xrange(n):
		RPI[i] = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]
		print RPI[i]

fin.close()
fout.close()
