f = open('input.in', 'r')
numcases = int(f.readline())
for i in xrange(numcases):
	vol1 = int(f.readline())-1
	set1 = [f.readline().replace('\n','').split(' '),f.readline().replace('\n','').split(' '),f.readline().replace('\n','').split(' '),f.readline().replace('\n','').split(' ')]
	vol2 = int(f.readline())-1
	set2 = [f.readline().replace('\n','').split(' '),f.readline().replace('\n','').split(' '),f.readline().replace('\n','').split(' '),f.readline().replace('\n','').split(' ')]
	vol1row = set1[vol1]
	vol2row = set2[vol2]
	numMatches = 0
	val = ""
	for y in vol1row:
		for z in vol2row:
			if y == z:
				numMatches = numMatches + 1
				val = y
	if numMatches == 1:
		print "Case #"+str(i+1)+": "+val
	if numMatches > 1:
		print "Case #"+str(i+1)+": Bad magician!"
	if numMatches == 0:
		print "Case #"+str(i+1)+": Volunteer cheated!"