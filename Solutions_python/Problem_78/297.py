fileName = "A-small-attempt1"
#fileName = "A-sample"
fin = open(fileName + ".in", "r")
fout = open(fileName + ".out", "w")

T = int(fin.readline())

for caseID in xrange(1, T+1):
	ans = False
	N, pd, pg = map(int, fin.readline().split())
	if ((pd == 100) and (pg != 100)) or ((pd != 100) and (pg == 100)):
		ans == False
	elif ((pd == 0) and (pg != 0)) or ((pd != 0) and (pg == 0)):
		ans == False
	else:
		nd = numerator(pd/100)
		D = denominator(pd/100)
		ng = numerator(pg/100)
		G = denominator(pg/100)
		a = nd
		b = D
		while D + b < N:
			nd += a
			D += b
		a = ng
		b = G
		while (G < D) or (G - ng < D - nd) or (ng < nd):
			ng += a
			G += b
		print N, nd, D, ng, G
		if (D <= N) and (nd <= ng) and (D - nd <= G - ng):
			ans = True
	if ans:
		print "Case #%d: Possible" % caseID
		fout.write("Case #%d: Possible\n" % caseID)
	else:
		print "Case #%d: Broken" % caseID
		fout.write("Case #%d: Broken\n" % caseID)
	

fin.close()
fout.close()
