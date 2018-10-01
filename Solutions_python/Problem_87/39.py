import sys

file = open("A-large.in")
#file = open("a.test")
strWholeFile = file.read()
aStrLines = strWholeFile.split("\n")

nCases = int(aStrLines[0])
aStrLinesLeft = aStrLines[1:]

for nCase in range(1, nCases + 1):
	print >> sys.stderr, "On case " + str(nCase) + " of " + str(nCases)
	
	aStrTok = aStrLinesLeft[0].split()
	
	sTot = float(aStrTok[0])
	sPlain = sTot
	dsWalk = float(aStrTok[1])
	dsRun = float(aStrTok[2])
	dtRun = float(aStrTok[3])
	nWalkways = int(aStrTok[4])
	
	lTupWalkways = []
	
	for i in range(nWalkways):
		aStrTok = aStrLinesLeft[1 + i].split()
		sStart = float(aStrTok[0])
		sEnd = float(aStrTok[1])
		dds = float(aStrTok[2])
		
		sLength = sEnd - sStart
		sPlain -= sLength
		
		lTupWalkways = lTupWalkways + [(dds, sLength)]
		
	aStrLinesLeft = aStrLinesLeft[nWalkways + 1:]
		
	lTupWalkways = lTupWalkways + [(0, sPlain)]
	lTupWalkways.sort()
	
	#print >> sys.stderr, "Sorted tuples: " + str(lTupWalkways)
	
	dtTotal = 0.0
	
	for tup in lTupWalkways:
		(dds, s) = tup
		#print "On " + str(tup) + "; ran for " + str(dtTotal)
		
		if dtRun > 0.0:
			ds = dsRun + dds
			
			if ds * dtRun > s:
				dt = s / ds
				#print "Running for: " + str(dt)
				dtRun -= dt
				dtTotal += dt
				s = 0.0
			else:
				#print "Running max: " + str(dtRun)
				s -= ds * dtRun
				dtTotal += dtRun
				dtRun = 0.0
				
		if s > 0.0:
			ds = dsWalk + dds
			dt = s / ds
			#print "Walking; dist is " + str(s) + "; speed is " + str(ds) + "; it takes " + str(dt)
			dtTotal += dt
			
	print "Case #" + str(nCase) + ": " + str(dtTotal)