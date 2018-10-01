import codecs
with codecs.open("A-small-attempt1.in", "r", "utf- 8") as f:
	temp = f.readlines()
	c = 0
	for x in temp[1:]:
		t = x.strip().split()
		if len(t) <= 1:
			continue
		c += 1
		t = [int(z) for z in t]
#		t.sort()
		N, PD, PG = t
		if PG == 100 and PD != 100:
			print "Case #{0}: Broken".format(c)
		elif PG == 0 and PD != 0:
			print "Case #{0}: Broken".format(c)
		else:
			T = 100
			if PD % 2 == 0:
				PD = PD / 2
				T = T / 2
			if PD % 2 == 0:
				PD = PD / 2
				T = T / 2
			if PD % 5 == 0:
				PD = PD / 5
				T = T / 5
			if PD % 5 == 0:
				PD = PD / 5
				T = T / 5

			GP = 100
			if PG % 2 == 0:
				PG /= 2
				GP /= 2
			if PG % 2 == 0:
				PG /= 2
				GP /= 2
			if PG % 5 == 0:
				PG /= 5
				GP /= 5
			if PG % 5 == 0:
				PG /= 5
				GP /= 5

			flag = False
			for x in xrange(1, N / T + 1):
				y = 1
				while True:
					if GP * y < T * x:
						y += (T * x - GP * y) / GP
						continue
					if PG * y < PD * x:
						y += (PD * x - PG * y) / PG
						continue
					if GP * y - (T * x) >= 0 and PG * y - PD * x >= 0:
						flag = True
						break
					y += 1
				if flag:
					break;
					
			if flag:
				print "Case #{0}: Possible".format(c)
			else:
				print "Case #{0}: Broken".format(c)
