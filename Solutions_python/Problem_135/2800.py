with open("A-small-attempt0.in", "r") as infile:
	cases = int(infile.readline())
	for casenum in xrange(cases):
		guess = int(infile.readline())
		for i in xrange(4):
			words = infile.readline()
			if i + 1 == guess:
				r1 = words.split()
		guess = int(infile.readline())
		for i in xrange(4):
			words = infile.readline()
			if i + 1 == guess:
				r2 = words.split()
		correct = []
		for i in r1:
			if i in r2:
				correct.append(i)
		if len(correct) == 0:
			cstring = "Volunteer cheated!"
		elif len(correct) > 1:
			cstring = "Bad magician!"
		else:
			cstring = correct[0]
		print "Case #%s: %s"%(casenum + 1, cstring)
				
		