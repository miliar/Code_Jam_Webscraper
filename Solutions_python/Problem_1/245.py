def doCase(fi, fo, caseIdx):
	numEngines = int(fi.readline())
	engines = []
	for i in range(numEngines):
		engines.append(fi.readline().strip("\n"))
	numQueries = int(fi.readline())
	queries = []
	for i in range(numQueries):
		queries.append(fi.readline().strip("\n"))

	touch = list(engines)
	numSwitches = 0
	for i in range(numQueries):
		if len(touch) == 1:
			if queries[i] in touch:
				touch = list(engines)
				touch.remove(queries[i])
				numSwitches = numSwitches + 1
				#print "Switched at %d" % i
		else:
			if queries[i] in touch:
				touch.remove(queries[i])
				
	fo.write("Case #%d: %d\n" % (caseIdx, numSwitches))

fi = open("A-large.in", "r")
fo = open("A-large.out", "w")
numCases = int(fi.readline())
for i in range(numCases):
	doCase(fi, fo, i+1)
fi.close()
fo.close()
