import sys
T = int(sys.stdin.readline())
for index in range(T):
	c1 = int(sys.stdin.readline())
	m1 = [map(lambda x: int(x), sys.stdin.readline().split()) for i in range(4)]
	c2 = int(sys.stdin.readline())
	m2 = [map(lambda x: int(x), sys.stdin.readline().split()) for i in range(4)]
	s = set(m1[c1-1]) & set(m2[c2-1])
	l = len(s)
	if (l == 1):
		print "Case #"+str(index+1)+": "+str(list(s)[0])
	elif l > 1:
		print "Case #{}: Bad magician!".format(str(index+1))
	elif l == 0:
		print "Case #{}: Volunteer cheated!".format(str(index+1))

