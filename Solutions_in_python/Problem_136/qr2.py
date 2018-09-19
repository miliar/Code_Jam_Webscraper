
inf = open("B-large.in")
of = open("output1.txt",'w')
t = int(inf.readline())
for i in range(t):
	c, f, x = inf.readline().split(' ')
	c = float(c)
	f = float(f)
	x = float(x)
	print c,f,x
	r = 2.0
	cs = x / r
	ls = x / r
	s = 0.
	while True:
		ls = cs
		cs = s + c / r + x / (r + f)
		if cs < ls:
			s += c / r
			r += f
		else:
			s += x / r
			break
	of.write(str("Case #%d: %7f\n") % (i+1, s))
of.close()