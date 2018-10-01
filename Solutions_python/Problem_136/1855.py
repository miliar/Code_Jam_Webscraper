f = open("b.in", "r")
d = f.read()
f.close()

def solve(c,f,x):
	t = 0.0
	r = 2.0
	_t = -1.0
	while True:
		tx = x / r
		tf = c / r
		if _t < 0.0: _t = t+tx
		elif t+tx > _t: return "%.7f" % (_t)
		_t = t+tx
		t += tf
		r += f

d = d.split("\n")[1:-1]

f = open("b.out", "w")
for i in xrange(len(d)):
	l = d[i].split(" ")
	l = [float(v) for v in l]
	s = "Case #%d: %s" % (i+1, solve(l[0],l[1],l[2]))
	print s
	f.write(s+"\n")
f.close()

