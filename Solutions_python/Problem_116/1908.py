import sys


if __name__=='__main__':
	f = open(sys.argv[1], 'r')
	T = int(f.readline()[:-1])
	for case_no in range(1, T + 1):
		G = []
		for i in range(4):
			G.append(list(f.readline()[:-1]))
		checks = []
		has_blank = False
		for i in range(4):
			r = set()
			c = set()
			for j in range(4):
				if G[i][j] == '.':
					has_blank = True
				r.add(G[i][j])
				c.add(G[j][i])
			checks.append(r)
			checks.append(c)
		d1 = set([G[0][0], G[1][1], G[2][2], G[3][3]])
		d2 = set([G[0][3], G[1][2], G[2][1], G[3][0]])
		checks.append(d1)
		checks.append(d2)
		status = ''
		for check in checks:
			if 'X' in check and 'O' not in check and '.' not in check:
				status = 'X won'
				break
			elif 'O' in check and 'X' not in check and '.' not in check:
				status = 'O won'
				break
		if status == '':
			if has_blank:
				status = 'Game has not completed'
			else:
				status = 'Draw'
		print "Case #%s: %s" % (case_no, status)
		f.readline()
	
