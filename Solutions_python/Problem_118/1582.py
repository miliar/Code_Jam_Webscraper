def indb(fdb):
	r = []
	n = int(fdb.readline())
	for i in range(n):
		r.append(int(fdb.readline()[:-1]))
	return r

def input(fin):
	t = fin.readline().split(' ')
	s = int(t[0])
	t = int(t[1])
	return s, t

def process(t, db):
	s, t = t
	r = 0
	for i in db:
		if s <= i and i <= t:
			r = r + 1
	return str(r)

def output(fout, res):
	fout.write(res + '\n')

db = indb(open('pal.in'))
fin = open('2.in')
fout = open('2.out', 'w')
t = int(fin.readline())
for i in range(t):
	output(fout, 'Case #%d: ' % (i + 1) + process(input(fin), db))