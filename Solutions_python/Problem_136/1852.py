import fileinput

def solve(c, f, x):
	s, k = 0, 0
	p = x/2
	while True:
		s += c/(k*f+2)
		k += 1
		v = s + x/(k*f+2)
		if v > p: return p
		p = v

f = fileinput.input()
for t in range(1, 1+int(f.readline())):
	c, s, x = list(map(float, f.readline().rstrip().split()))
	print("Case #%d: %.7f" % (t, solve(c, s, x)))