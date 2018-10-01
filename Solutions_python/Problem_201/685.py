

inf = open("c.in", 'r')
outf = open("c.out", 'w')

t = int(inf.readline())

for tc in xrange(0, t):
	n, k = map(long, inf.readline().split())
		
	pow2 = 1
	while (2 * pow2 <= k):
		pow2 *= 2	
	m2 = (n - k + pow2) / pow2	
	
	'''
	dists = [n]
	for i in xrange(0, k - 1):
		m = max(dists)
		dists.append(m / 2)
		if (m % 2 == 1):			
			dists.append(m / 2)
		else:
			dists.append(m / 2 - 1)
		dists.remove(m)	
	m = max(dists)'''
	m = m2
	
	
		
	maxd = m / 2
	mind = m  - 1 - maxd
	outf.write("Case #" + str(tc + 1) + ": ")	
	outf.write(str(maxd) + " " + str(mind) + "\n")	
		
	
outf.close()
