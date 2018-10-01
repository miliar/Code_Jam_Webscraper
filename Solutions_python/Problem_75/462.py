import sys; _tokens = sys.stdin.read().split(); _next_token = -1
def next(): global _next_token; _next_token += 1; return _tokens[_next_token]

def testcase(id):
	combines = {}
	opposes = {}
	nc = int(next())
	for i in xrange(nc):
		t = next()
		combines.setdefault(t[0], {})
		combines.setdefault(t[1], {})
		combines[t[0]][t[1]] = t[2]
		combines[t[1]][t[0]] = t[2]
	nc = int(next())
	for i in xrange(nc):
		t = next()
		opposes[t[0]] = t[1]
		opposes[t[1]] = t[0]
	next()
	clist = []
	for i in next():
		if not clist:
			clist.append(i)
		else:
			g = i in combines and combines[i].get(clist[-1])
			if g:
				clist[-1] = g
			else:
				o = opposes.get(i)
				if o and o in clist:
					clist = []
				else:
					clist.append(i)
	print "Case #{0}: [{1}]".format(id, ', '.join(clist))

ncases = int(next())
for i in xrange(ncases):
	testcase(i+1)
