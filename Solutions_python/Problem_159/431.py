f = file('A-large.in','r')

lines = f.readlines()
T = int(lines[0].strip())

def run(ints, snaps):
	sum1 = 0
	for i in xrange(0,len(snaps)-1):
		sum1 += max(0, snaps[i] - snaps[i+1])

	sum2 = 0
	max_rate = None
	for i in xrange(0,len(snaps)-1):
		rate = max(0, snaps[i] - snaps[i+1])
		if max_rate == None or rate > max_rate:
			max_rate = rate

	for j in xrange(0,len(snaps)-1):
		sum2 += min(max_rate,snaps[j])

	return sum1, sum2

for i in xrange(0,T):
	ints = int(lines[2*i+1].strip())
	snaps = [int(j) for j in lines[2*i+2].strip().split(' ')]
	sum1, sum2 = run(ints, snaps)
	print "Case #%d: %d %d" % (i+1, sum1, sum2)