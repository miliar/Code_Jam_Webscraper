
def is_palin(x):
	s = str(x)
	return s == s[::-1]

a = []

def check(s):
	if is_palin(s) and is_palin(int(s) ** 2):
		a.append(int(s))

def go(s, c1):
	if s:
		check(s + s[::-1])
	for x in xrange(3):
		check(s + str(x) + s[::-1])

	if len(s) < 26:
		for x in xrange(2 if c1 < 4 else 1):
			if s or x > 0:
				go(s + str(x), c1 + x)


go("", 0)

for z in xrange(26):
	for x in xrange(3):
		s = "2" + "0"*z + str(x) + "0"*z + "2"
		check(s)


check(3)
check(22)

sq = [x*x for x in a]

tc = int(raw_input())
for t in xrange(tc):
	A, B = map(int, raw_input().split())
	ans = 0
	for x in sq:
		if x >= A and x <= B:
			ans += 1
	print "Case #{}: {}".format(t + 1, ans) 