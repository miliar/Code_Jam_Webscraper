ins = open( "A-small-attempt0.in", "r" )
input = []
for line in ins:
    input.append( line.strip() )

ins.close()

numCases = input[0]
for i in range(0,int(numCases)):
	rowSelection = int(input[10*i + 1])
	rowSelection2 = int(input[10*i + 6])
	set1 = input[rowSelection+10*i+1].split(" ")
	set2 = input[rowSelection2+10*i+5+1].split(" ")
	intersect = [val for val in set1 if val in set2]
	if len(intersect) > 1:
		print "Case #" + str(i+1) + ": Bad magician!"
	elif len(intersect) == 0:
		print "Case #" + str(i+1) + ": Volunteer cheated!"
	else:
		print "Case #" + str(i+1) + ": "+ intersect[0]