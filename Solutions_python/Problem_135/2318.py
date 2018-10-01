
def intersect(a,b) :
	return list(set(a) & set(b))

file_in = open('C:\\Users\\ichung\\Downloads\\code\\A-small-attempt0.in','r')
numSets = int(file_in.readline())
# print numSets
for i in xrange(1,numSets+1) :
	# print 'loop'
	firstBlockRow = int(file_in.readline())
	# print firstBlockRow

	if(firstBlockRow == 1) :
		firstRow = file_in.readline()
	else :
		file_in.readline()

	if(firstBlockRow == 2) :
		firstRow = file_in.readline()
	else :
		file_in.readline()

	if(firstBlockRow == 3) :
		firstRow = file_in.readline()
	else :
		file_in.readline()

	if(firstBlockRow == 4) :
		firstRow = file_in.readline()
	else :
		file_in.readline()

	firstRow = firstRow[:-1]
	firstRowSeparated = firstRow.split()
	# print firstRow
	# print firstRowSeparated

	secondBlockRow = int(file_in.readline())
	# print secondBlockRow

	if(secondBlockRow == 1) :
		secondRow = file_in.readline()
	else :
		file_in.readline()

	if(secondBlockRow == 2) :
		secondRow = file_in.readline()
	else :
		file_in.readline()

	if(secondBlockRow == 3) :
		secondRow = file_in.readline()
	else :
		file_in.readline()

	if(secondBlockRow == 4) :
		secondRow = file_in.readline()
	else :
		file_in.readline()

	secondRow = secondRow[:-1]
	secondRowSeparated = secondRow.split()
	# print secondRow
	# print secondRowSeparated

	rowInter = intersect(firstRowSeparated, secondRowSeparated)
	# print rowInter

	if(len(rowInter) == 1) :
		print "Case #" + str(i) + ": " + rowInter[0]
	elif(len(rowInter) > 1) :
		print "Case #" + str(i) + ": Bad magician!"
	else :
		print "Case #" + str(i) + ": Volunteer cheated!"



