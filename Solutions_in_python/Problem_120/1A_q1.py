import sys
sys.stdin = open("A-small-attempt0.in", "r")
sys.stdout = open("A-small-attempt0.out", "w")
for i in range(input()):
	r, t = map(int, raw_input().split())
	#print t, r
	ans = ((1 - 2 * r) + ((2 * r - 1) ** 2 + 8 * t) ** 0.5) / 4
	print "Case #%d: %d" % (i+1, ans)
