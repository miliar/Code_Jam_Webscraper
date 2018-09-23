def f(ticketlist,coastersize):
	count = [0,0]
	coaster = []
	for n in range(coastersize):
		coaster.append(0)
	for ticket in ticketlist:
		coaster[ticket[0] - 1] += 1
		count[ticket[1] - 1] += 1
	desiredrides = max(count)
	if coaster[0] > desiredrides:
		return [coaster[0],0]
	for n in range(1,len(coaster)):
		if coaster[n] > desiredrides:
			return [desiredrides,coaster[n]-desiredrides]
	return [desiredrides,0]

import sys
with open(sys.argv[1], "r") as fileIN:
	inputLines = fileIN.readlines()
		
with open(sys.argv[2], "w") as fileOUT:
	numberOfCases = int(inputLines.pop(0))
	for num in range(numberOfCases):
		coastersize,customers,tickets = [int(x) for x in inputLines.pop(0).rstrip().split()]
		ticketlist = []
		for i in range(tickets):
			ticketlist.append([int(x) for x in inputLines.pop(0).rstrip().split()])
		output = f(ticketlist,coastersize)
		fileOUT.write('Case #' + str(num+1) + ': ' + str(output[0]) + ' ' + str(output[1]) + '\n')