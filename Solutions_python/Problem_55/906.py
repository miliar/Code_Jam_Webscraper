cases = int(raw_input())
for cena in xrange(1,cases+1):
	tmp = raw_input()
	vec = raw_input()
	r = int(tmp.split()[0])
	k = int(tmp.split()[1])
	n = int(tmp.split()[2])

	vec = [int(a) for a in vec.split()]
	nv = [i for i in vec]
	euro = 0
	j = 0
	run = r
	registo = []

	while r>0:
		c = k
		trip = 0
		j+=1
		nl = []
		
		while len(nv)>0 and c - nv[0] >= 0:
			c = c - nv[0]	
			euro += nv[0]
			nl = nl + [nv[0]]
			nv = nv[1:]
		registo.append(euro)	
		nv = nv + nl
		if nv == vec:
			break
		r-=1
	if j== run:
		print "Case #"+str(cena)+": "+str(euro)
	else:
		if run%j != 0:
			euro = euro*int(run/j) + registo[(run%j)-1]
		else:
			euro = euro*int(run/j)
		print "Case #"+str(cena)+": "+str(euro)
