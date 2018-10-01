import sys

def f(L,P,C):
	testspots=0
	x=L*C
	while x<P:
		testspots += 1
		x = x*C
	
	c2 = 0
	while testspots>0:
		testspots -= 1
		testspots = (testspots / 2) + (testspots % 2)
		c2 += 1		
	
	return c2

inf = open(sys.argv[1])
T = int(inf.readline())
for i in range(T):
	L,P,C = [int(x) for x in inf.readline().split()]
	result = f(L,P,C)
	print "Case #%d: %d" % (i+1, result)
