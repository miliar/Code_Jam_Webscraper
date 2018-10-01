
numLawns = input()

# print numLawns
for lawnNum in xrange(0, numLawns):
	size = [int(x) for x in raw_input().split(" ")]

	lawn = [[]]*size[0]
	maxRows = [0]*size[0]
	maxCols = [0]*size[1]

	for i in xrange(0, size[0]):
		lawn[i] = [int(x) for x in raw_input().split(" ")]
		maxRows[i] = max(lawn[i])

	for j in xrange(0, size[1]):
		m = 0;
		for i in xrange(0, size[0]):
			m = max(m, lawn[i][j])
		maxCols[j] = m
	i = 0

	# for line in lawn:
	# 	print line, maxRows[i]
	# 	i += 1
	# print maxCols 

	fail = False
	for i in xrange(0, size[0]):
		for j in xrange(0, size[1]):
			if lawn[i][j] != maxRows[i] and lawn[i][j] != maxCols[j]:
				fail = True
				break
		if fail:
			break

	print "Case #%d: %s" % (lawnNum + 1, "NO" if fail else "YES")