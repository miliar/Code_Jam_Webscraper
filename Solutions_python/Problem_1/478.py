f = open('file.txt')
cases = int(f.readline())
for i in range(cases):
	n = int(f.readline())
	for j in range(n):
		f.readline()
	s = set()
	numchanges = 0
	for j in range(int(f.readline())):
		line = f.readline()
		if line in s:
			continue
		if len(s) < n-1:
			s.add(line)
			continue
		else:
			s = set()
			s.add(line)
			numchanges +=1
	print "Case #%d: %d" % (i+1, numchanges)


