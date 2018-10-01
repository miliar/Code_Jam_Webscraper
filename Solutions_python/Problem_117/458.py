for T in xrange(int(raw_input())):
	s = map(int, raw_input().split())
	N = s[0]
	M = s[1]
	lawn = [[0]*M for _ in xrange(N)]
	possible = [[False]*M for _ in xrange(N)]
	for i in xrange(N):
		s = map(int, raw_input().split())
		for j in xrange(M):
			lawn[i][j] = s[j]
	#check rows
	for i in xrange(N):
		max = 0
		for j in xrange(M):
			if lawn[i][j]>max: max = lawn[i][j]
		for j in xrange(M):
			if lawn[i][j] == max: possible[i][j] = True
	#check cols
	for j in xrange(M):
		max = 0
		for i in xrange(N):
			if lawn[i][j]>max:max = lawn[i][j]
		for i in xrange(N):
			if lawn[i][j] == max: possible[i][j] = True
	#debug, write possible
	for i in xrange(N):
		s = "";
		for j in xrange(M):
			if possible[i][j]:
				s+="T"
			else:
				s+="F"
#		print s
	#output result
	result = "YES"
	for i in xrange(N):
		for j in xrange(M):
			if not possible[i][j]: result = "NO"
	print "Case #"+str(T+1)+": " + result
