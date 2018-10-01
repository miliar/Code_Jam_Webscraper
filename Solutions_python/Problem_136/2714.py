import sys

def get_cookies(c, f, x):
	time = 0.0
	cps = 2.0 # cookies per second
	# x can be reached faster, if we build a new cookie farm
	while x / cps > (c / cps + x / (cps + f)): 
		time += c / cps
		cps += f
	time += x / cps
	return time

if __name__ == "__main__":
	f = sys.stdin
	T = int(f.readline())
	for i in xrange(T):
		C, F, X = [float(x) for x in f.readline().split()][:3]
		print "Case #%d: %.7f" % (i + 1, get_cookies(C, F, X))