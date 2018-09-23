import sys

lines = open(sys.argv[1], "rb").read().splitlines()

i = 1
case = 0
res = ""
while i < len(lines):
	case += 1
	d, n = map(int, lines[i].split())
	i += 1
	max_t = 0
	for j in xrange(n):
		k, s = map(int, lines[i + j].split())
		t = (d - k) / float(s)
		if t > max_t:
			max_t = t
	i += n
	res += "Case #%d: %.6f\n" % (case, d / max_t)

open(sys.argv[2], "wb").write(res)
