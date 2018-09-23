import sys

lines = open(sys.argv[1], "rb").read().splitlines()

res = ""
for case, line in enumerate(lines[1:]):
	n, r, o, y, g, b, v = map(int, line.split())
	total = sum([r, y, b])
	l = [[r, "R"], [y, "Y"] ,[b, "B"]]
	l = [x for x in l if x[0] > 0]
	solution = ""
	for i in xrange(total - 2):
		l.sort()
		l.reverse()
		idx = 0
		if i == 0 or solution[-1] != l[0][1]:
			idx = 0
		elif len(l) == 1:
			solution = "IMPOSSIBLE"
			break
		else:
			idx = 1
		solution += l[idx][1]
		l[idx][0] -= 1
		if l[idx][0] == 0:
			l.pop(idx)
	if solution != "IMPOSSIBLE":
		if len(l) == 1:
			solution = "IMPOSSIBLE"
		else:
			r = (solution[-1], solution[0])
			cc = (l[0][1], l[1][1])
			if cc[0] != r[0] and cc[1] != r[1]:
				solution += cc[0]
				solution += cc[1]
			elif cc[1] != r[0] and cc[0] != r[1]:
				solution += cc[1]
				solution += cc[0]
			else:
				solution = "IMPOSSIBLE"

	res += "Case #%d: %s\n" % (case + 1, solution)

open(sys.argv[2], "wb").write(res)
