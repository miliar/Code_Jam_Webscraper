import fileinput

f = fileinput.input()
nt = int(f.readline().strip())
for t in range(nt):
	C, F, X = (float(x) for x in f.readline().strip().split())
	w = ((X - C) * F) / C
	cps = 2.0
	m = 0.0
	while 1:
		if cps < w:
			m += C/cps
			cps += F
		else:
			m += X/cps
			break
	print 'Case #%s: %s' % (t+1, m)










