import fileinput

input = fileinput.input()
rl = lambda : input.readline()
count = int(input.readline())
for n in range(count):
	row = int(rl()) - 1
	case1 = [map(int, rl().split()) for r in range(4)][row]
	row = int(rl()) - 1
	case2 = [map(int, rl().split()) for r in range(4)][row]
	vals = []
	for v in case1:
		if v in case2:
			vals.append(v)
	if len(vals) == 0:
		print "Case #%d: Volunteer cheated!" % (n+1,)
	elif len(vals) > 1:
		print "Case #%d: Bad magician!" % (n+1,)
	else:
		print "Case #%d: %d" % (n+1, vals[0])