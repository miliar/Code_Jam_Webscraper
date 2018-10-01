def paint_amount(r):
	area = (2*r)-1 
	return area
def pr(r,t):
	rings = 0
	r += 1
	while t - paint_amount(r) >= 0:
		t -= paint_amount(r)
		r+=2
		rings+=1
	return rings

for testcase in xrange(input()):
	r,t = map(int, raw_input().split())
	print "Case #%d: %d" % (1 + testcase, pr(r,t))
