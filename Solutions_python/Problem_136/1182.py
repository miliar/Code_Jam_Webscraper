def probB():
	filename = "B-large.in.txt"
	f = open(filename)
	cases = int(f.readline())
	results = []
	for i in range(cases):

		rate = 2 # initial cookie rate
		parameters = f.readline().split()
		
		farmCost = float(parameters[0])
		addRate = float(parameters[1])
		goal = float(parameters[2])

		t, foundSol = 0.0, False # initial time
		while not(foundSol):
			timeNoFarm = t + (goal / rate) # time to goal at current rate
			
			timeToFarm = t + (farmCost / rate)
			timeWithFarm = timeToFarm + (goal / (rate + addRate))

			if timeNoFarm < timeWithFarm:
				results.append(round(timeNoFarm, 7))
				print "Done."
				foundSol = True
			else:
				t = timeToFarm
				rate = rate + addRate
	
	writeResults(results)





def writeResults(results):
	outfile = open("probBResults.txt", "w")
	for i in range(1, len(results) + 1):
		outfile.write("Case #%i: %s\n" % (i, results[i-1]))
	outfile.close()

probB()