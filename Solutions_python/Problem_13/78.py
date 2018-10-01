fin = open("input.txt", "r")
fout = open("output.txt", "w")

def f_or(x,y):
	return x | y

def f_and(x,y):
	return x & y

for curCase in xrange(1, int(fin.readline()) + 1):
	(nodeCount, value) = map(int, fin.readline().split())
	nodes = []
	changeable = []
	vals = [0] * nodeCount
	for i in xrange((nodeCount - 1) / 2):
		(t, chfl) = fin.readline().split()
		first = (i + 1) * 2 - 1
		#nodes.append(f_or if  t == "0" else f_and)
		if chfl == "1" and value == int(t):
			changeable.append((i, f_or if  t == "0" else f_and))
			nodes.append((f_or if  t == "1" else f_and, first, first + 1))
		else:
			nodes.append((f_or if  t == "0" else f_and, first, first + 1))
	for i in xrange((nodeCount - 1) / 2, nodeCount):
		vals[i] = (0 if fin.readline().strip() == "0" else 1)
	for i in reversed(xrange((nodeCount - 1) / 2)):
		vals[i] = nodes[i][0](vals[nodes[i][1]], vals[nodes[i][2]])
	if vals[0] <> value:
		fout.write("Case #%i: IMPOSSIBLE\n" % curCase)
	else:
		result = 0
		for i in reversed(xrange(len(changeable))):
			vals[changeable[i][0]] = changeable[i][1](vals[nodes[changeable[i][0]][1]], vals[nodes[changeable[i][0]][2]])
			for j in reversed(xrange((changeable[i][0] + 1) // 2)):
				vals[j] = nodes[j][0](vals[nodes[j][1]], vals[nodes[j][2]])
			if vals[0] <> value:
				vals[changeable[i][0]] = value
				result += 1
		fout.write("Case #%i: %d\n" % (curCase, result))
fin.close()
fout.close()