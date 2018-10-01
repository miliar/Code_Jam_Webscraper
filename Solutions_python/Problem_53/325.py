import sys

if __name__ == "__main__":
	T = int(raw_input().strip())
	caseNumber = 1
	for X in xrange(1, T+1):
		a, b = (int(i) for i in raw_input().strip().split())
		ans = (b&((1<<a)-1)) == (1<<a)-1 and "ON" or "OFF"
		print "Case #%d: %s" % (X, ans)
