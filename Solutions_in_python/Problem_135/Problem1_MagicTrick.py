def GetCase(n):
	nChosenRow1 = int(raw_input())
	Cards1 = [None, None, None, None]
	for x in xrange(4):
		input = raw_input()
		Cards1[x] = [int(y) for y in input.split(' ')]
			
	nChosenRow2 = int(raw_input())
	Cards2 = [None, None, None, None]
	for x in xrange(4):
		input = raw_input()
		Cards2[x] = [int(y) for y in input.split(' ')]
	
	s1 = set(Cards1[nChosenRow1 - 1])
	s2 = set(Cards2[nChosenRow2 - 1])
	
	s = s1.intersection(s2)
	
	if len(s) == 1:
		print "Case #%d: %d" % (n, s.pop())
	elif len(s) > 1:
		print "Case #%d: Bad magician!" % (n)
	elif len(s) == 0:
		print "Case #%d: Volunteer cheated!" % (n)
		
nTestCases = int(raw_input())

for i in xrange(nTestCases):
	GetCase(i + 1)