t = int(raw_input())

for time in xrange(t):
	n = int(raw_input())
	naomi = map(float,raw_input().split())
	ken = map(float,raw_input().split())
	
	naomi.sort()
	ken.sort()

	naomi2 = list(naomi)
	ken2 = list(ken)

	des = 0
	pos = 0
	
	# possible

	mem = {}

	ps = len(ken)
	ps2 = ps
	for i in xrange(n):
		checker = naomi[i]
		for j in xrange(ps):
			if ken[j] > checker :
				ps -= 1
				del ken[j]
				break
	
	#des
	for i in xrange(n):
		checker = naomi2[i]
		if ken2[des] < checker:
			des += 1

	pos = len(ken)

	print "Case #" + str(time+1) + ":" ,
	print des,pos
