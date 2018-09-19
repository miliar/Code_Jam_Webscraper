import os, sys, array

#######################################
def timeToMinutes(time):
	temp = time.split(":")
	return int(temp[0]) * 60 + int(temp[1])

#######################################
def process(turnAroundTime, listAB, listBA):
	#print "Engines:", listEngines
	#print "Steps:", listSteps
	
	# Sorted lists
	departuresA = []
	departuresB = []
	arrivalsA = []
	arrivalsB = []
	
	for item in listAB:
		departuresA.append( timeToMinutes(item[0])  )
		arrivalsB.append( timeToMinutes(item[1]) + turnAroundTime )
		
	for item in listBA:
		departuresB.append( timeToMinutes(item[0]) )
		arrivalsA.append( timeToMinutes(item[1]) + turnAroundTime )
		
	departuresA.sort()
	departuresB.sort()
	arrivalsA.sort()
	arrivalsB.sort()

	#  Total trains departing
	needA = len(departuresA)
	needB = len(departuresB)
	
	# Try to reuse arriving trains
	for dep in departuresA:
		if len(arrivalsA) > 0:
			if arrivalsA[0] <= dep:
				needA -= 1
				arrivalsA.pop(0)
			
	for dep in departuresB:
		if len(arrivalsB) > 0:
			if arrivalsB[0] <= dep:
				needB -= 1
				arrivalsB.pop(0)
	
	return needA,needB

#######################################
file = open("test.in.txt", "r");
fileOut = open("test.out.txt", "w");

numTasks = int(file.readline())

# ------------
for taskIndex in range(0,numTasks):
	#print "---------------"
	#print "---------------"
	#print "---------------"
	#print "--- Task", taskIndex+1
	
	turnAroundTime = int(file.readline())	
	
	tmp = file.readline().strip().split(" ")
	numAB = int(tmp[0])
	numBA = int(tmp[1])
	
	#print "T =", turnAroundTime
	#print "AB =", numAB
	#print "BA =", numBA
	
	listAB = []
	for i in range(0,numAB):
		listAB.append( file.readline().strip().split(" ") )
		
	listBA = []
	for i in range(0,numBA):
		listBA.append( file.readline().strip().split(" ") )
		
	#print "A to B:", listAB
	#print "B to A:", listBA
	
	totalResultA, totalResultB = process(turnAroundTime, listAB, listBA)
	print "Results:", totalResultA, "and", totalResultB
	
	fileOut.write("Case #" + str(taskIndex+1) + ": " + str(totalResultA) + " " + str(totalResultB) + "\n")
	fileOut.flush()
# ------------
	
fileOut.close()
file.close()


# output:
# Case #X: Y
#
# ie:
# Case #1: 1
# Case #2: 0
