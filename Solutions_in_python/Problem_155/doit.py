infile = open("test", 'r') # open file for appending
outfile = open("result","w") # open file for writing

firstLine = infile.readline()
case = 0
for line in infile:
	testcase = line.rstrip("\n").split(" ")
	case += 1
	shyiest = int(testcase[0])
	audience = testcase[1]

	# print testcase
	k = 0
	peopleToInvite = 0
	counter = 0
	while k < shyiest:
		counter += int(audience[k])
		if (counter < k+1): 
			invite = k+1 - counter
			peopleToInvite += invite
			counter += invite

		k += 1
	
	output = "Case #"+str(case)+": "+str(peopleToInvite)+"\n"
	outfile.write(output)


infile.close()
outfile.close()