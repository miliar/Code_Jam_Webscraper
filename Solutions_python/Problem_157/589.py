def check(s):
	b = 1
	d = [[[0,1],[1,1],[2,1],[3,1]],[[1,1],[0,-1],[3,1],[2,-1]],[[2,1],[3,-1],[0,-1],[1,1]],[[3,1],[2,1],[1,-1],[0,-1]]]
	cur = 0
	p = 0
	while p < len(s) and (cur != 1 or b != 1):
		if s[p] == "i":
			tmp = 1
		elif s[p] == "j":
			tmp = 2
		else:
			tmp = 3
		b = b*d[cur][tmp][1]
		cur = d[cur][tmp][0]
		p += 1
	if p == len(s):
		return False
	cur = 0
	b = 1
	while p < len(s) and (cur != 2 or b != 1):
		if s[p] == "i":
			tmp = 1
		elif s[p] == "j":
			tmp = 2
		else:
			tmp = 3
		b = b*d[cur][tmp][1]
		cur = d[cur][tmp][0]
		p += 1
	if p == len(s):
		return False
	cur = 0
	b = 1
	while p < len(s):
		if s[p] == "i":
			tmp = 1
		elif s[p] == "j":
			tmp = 2
		else:
			tmp = 3
		b = b*d[cur][tmp][1]
		cur = d[cur][tmp][0]
		p += 1
	if cur != 3 or b != 1:
		return False
	return True


f = open("Cin.txt","r")
g = open("Cout.txt","w")
t = int(f.readline())
for i in xrange(1,t+1):
	st = f.readline().split()
	l = int(st[0])
	x = int(st[1])
	ss = f.readline().strip("\n")
	s = []
	for j in xrange(x):
		for item in ss:
			s.append(item)
	if check(s):
		g.write("Case #%d: YES\n" % (i))
	else:
		g.write("Case #%d: NO\n" % (i))