import sys


t = int(sys.stdin.readline())

for case in xrange(t):
	nrow1 = int(sys.stdin.readline())
	row1=""
	for x in range(4):
		line = sys.stdin.readline().strip()
		linea = line.split(" ")
		if nrow1 == x+1:
			row1=set(linea)


	nrow2 = int(sys.stdin.readline())
	row2=""
	for x in range(4):
		line = sys.stdin.readline().strip()
		linea = line.split(" ")
		if nrow2 == x+1:
			row2=set(linea)
	ans=row1&row2
	if len(ans)==1:
		print "Case #%d: %s" % (case+1, ans.pop())
	elif len(ans)>1:
		print "Case #%d: %s" % (case+1, "Bad magician!")
	else:
		print "Case #%d: %s" % (case+1, "Volunteer cheated!")
	