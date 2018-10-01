def pancake (m, p):
	if m <= 0:
		return max(p) + 1
	t = m
	for j in p:
		if j > m:
			if j % m == 0:
				t += j // m - 1
			else:
				t += j // m
	return t

def average (p):
	return sum(p) // len(p)

infile = open("B-large.in")
outfile = open("output", "w")

ncases = int(infile.readline())

for i in xrange(0, ncases):
	outfile.write("Case #%d: " % (i + 1))

	d = int(infile.readline())
	p = map(int, infile.readline().strip(" \n").split(" "))

	# md = average(p) // 2
	m = max(p)

	# cm = md
	# ct = m
	# cmm = 0

	# while True:
	# 	t = pancake(cm, p)
	# 	if t > ct:
	# 		break
	# 	else:
	# 		ct = t
	# 		cmm = cm
	# 		cm += 1

	# cm = md
	# while True:
	# 	t = pancake(cm, p)
	# 	if t > ct:
	# 		break
	# 	else:
	# 		ct = t
	# 		cmm = cm
	# 		cm -= 1

	bt = m
	bm = 0
	for i in xrange(1, m):
		c = pancake(i, p)
		if c < bt:
			bt = c
			bm = i

	# print ct, pancake(cm, p)
	# print bt, pancake(bm, p)
	# print "\n"
	outfile.write("%d\n" % bt)
