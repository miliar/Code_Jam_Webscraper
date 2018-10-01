import sys
f = sys.stdin.readline

cases = int(f())
for c in xrange(cases):
	lst = map(int, f().split())
	n = lst[0]
	k = lst[1]
	k %= 2**n
	sol = "ON" if k == 2**n - 1 else "OFF"
	print 'Case #' + str(c + 1) + ': ' + sol
