f = open("b.in")
data = f.read()
f.close()

data = data.split("\n")

t = int(data[0])

def strLst(l):
	return "[" + ", ".join(l) + "]"

def comb(l, c1, c2):
	if len(l) < 2: return False
	if l[-1] == c1 and l[-2] == c2: return True
	if l[-1] == c2 and l[-2] == c1: return True
	return False

def solve(prods, ops, s):
	count = [0] * 256
	l = []
	
	for c in s:
		#print c,
		addC = True
		for prod in prods:
			if c in prod[:2] and comb(l + [c], prod[0], prod[1]):
				count[ord(l[-1])] -= 1
				l = l[:-1] + [prod[2]]
				count[ord(prod[2])] += 1
				addC = False
				#print l, "a"
				break
		
		if not addC: continue
		
		for op in ops:
			if c in op:
				if c == op[0] and count[ord(op[1])] > 0:
					l = []
					count = [0] * 256
					addC = False
					#print l, "b"
					break
				if c == op[1] and count[ord(op[0])] > 0:
					l = []
					count = [0] * 256
					addC = False
					#print l, "c"
					break
		if addC: 
			l += [c]
			count[ord(c)] += 1
		#print l
	
	return strLst(l)

f = open("b.out", "w")
for ti in xrange(t):
	l = data[ti+1].split(" ")
	
	c = int(l[0])
	C = l[1:c+1]
	d = int(l[c+1])
	D = l[c+2:c+d+2]
	s = l[-1]
	#print "--->", C, D, s
	
	S = "Case #%d: %s" % ((ti+1), solve(C, D, s))
	print S
	f.write("%s\n" % S)
f.close()

