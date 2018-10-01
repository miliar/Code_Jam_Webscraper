#Get input
t = int(raw_input().strip())
tests = []
for _ in xrange(t):
    tests.append(map(int, raw_input().strip().split()))

#do stuff
for i in xrange(t):
	k = tests[i][0]
	c = tests[i][1]
	s = tests[i][2]
	ans = " ".join([str(x+1) for x in xrange(k)])
	print "Case #{0}: {1}".format(i+1, ans)
