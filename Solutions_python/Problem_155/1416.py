
f = open('/home/nikita/cj/A-large.in', 'r')
tests = int(f.readline())
for t in range(0, tests):
	line = f.readline().split()
	g = int(line[0])
	s = line[1]
	guests = 0
	clapping = int(s[0])
	for i in range(1, len(s)):
	        if (clapping < i):
			guests = guests + (i - clapping)
			clapping = i
		clapping = clapping + int(s[i])
	print "Case #"+str(t+1) +": " + str(guests)
	
	
