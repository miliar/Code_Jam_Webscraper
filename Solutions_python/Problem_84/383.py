T = int(raw_input())

def findBlue(picture,R,C,startR):
	startC = 0
	for r in range(startR,R):
		for c in range(startC,C):
			if picture[r][c] == '#':
				return r,c
	return None,None

def makeSquareWith(picture,R,C,r,c):
	if r+1 == R or c+1 == C:
		return False
	if picture[r][c] == '#' and picture[r+1][c] == '#' and picture[r][c+1] == '#' and picture[r+1][c+1] == '#':
		picture[r][c] = '/'
		picture[r+1][c] = '\\'
		picture[r][c+1] = '\\'
		picture[r+1][c+1] = '/'
		return True
	else:
		return False

def solveCase(R,C,picture):
	#print "Should solve case : R: %d, C: %d" % (R, C)
	#print "Picture is : "
	#for r in range(0,R):
	#	print picture[r]
	foundABlue = False
	r,c = 0,0
	while(True):
		r, c = findBlue(picture,R,C,r)
		if r == c and r == None:
			break
		#print "Found blue at %d %d" % (r,c)
		if not makeSquareWith(picture,R,C,r,c):
			return False, picture
				
	return True, picture
		
for t in range(1,T+1):
	R, C = map(int,raw_input().split())
	picture = []
	for r in range(R):
		picture.append(list(raw_input()))
	possible,picture = solveCase(R,C,picture)
	if possible:
		print "Case #%d:" % (t)
		for l in picture:
			print ''.join(l)
	else:
		print "Case #%d:" % (t)
		print "Impossible"