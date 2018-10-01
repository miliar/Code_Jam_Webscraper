def gcd(a, b):
	if b == 0: return a
	return gcd(b, a % b)

def mcm(a, b):
	return a*b/gcd(a, b)

def nextMul(d, m):
	return m + ((d - (m % d)) % d)

f = open("a.in")
d = f.read()
f.close()

d = d.split("\n")

t = int(d[0])

f = open("a.out", "w")
for ti in xrange(t):
	l = d[ti+1].split(" ")
	l = [int(e) for e in l]
	
	n = l[0]
	pd = l[1]
	pg = l[2]
	
	D = 100 / gcd(100, pd)
	G = 100 / gcd(100, pg)
	
	prodG = nextMul(G, D)
	G *= prodG
	
	wD = pd / gcd(100, pd)
	wG = (pg / gcd(100, pg)) * prodG
	
	#print (wD, D), (wG, G)
	
	if 0 < D and D <= n and D <= G and wD <= wG and (D-wD) <= (G-wG):
		s = "Possible"
	else:
		s = "Broken"
	S = "Case #%d: %s" % ((ti+1), s)
	print S
	f.write("%s\n" % S)
f.close()

