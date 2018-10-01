
fname = "C-small-attempt0.in"

maxNum = 1000

palins = set()
fairs = []

def isPalin(n):
	s = str(n)
	rs = s[::-1]
	return s == rs

for i in range(1, maxNum):
	if isPalin(i):
		palins.add(i)

for it in palins:
	if it * it in palins:
		fairs.append(it * it)

with open(fname) as f:
	nCase = int(f.readline())
	for kase in range(0, nCase):
		left, right = map(lambda x:int(x), f.readline().split())
		print "Case #%d: %d" % (kase + 1, len(filter(lambda x:x >= left and x <= right, fairs)))
