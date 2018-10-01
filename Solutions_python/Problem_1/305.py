import os, sys, array

#######################################
def maxStepEngine(listEngines, listSteps):
	#print "---------------"
	#print "MAX STEP ENGINE"
	#print "Engines:", listEngines
	#print "Steps:", listSteps
	
	engineFirstEncounter = dict()
	for engine in listEngines:
		engineFirstEncounter[engine] = 0xFFFFFFFF
	
	stepIndex = 0
	for step in listSteps:
		if engineFirstEncounter[step] == 0xFFFFFFFF:
			engineFirstEncounter[step] = stepIndex
		stepIndex += 1
	
	maxSteps = -1
	bestEngine = ""
	for engine in engineFirstEncounter:
		if engineFirstEncounter[engine] > maxSteps:
			maxSteps = engineFirstEncounter[engine]
			bestEngine = engine
	
	#print "Output:", engineFirstEncounter
	#print "Best engine:", bestEngine
	#print "---------------"
	return bestEngine, engineFirstEncounter[bestEngine]
		
#######################################
def process(listEngines, listSteps):
	#print "Engines:", listEngines
	#print "Steps:", listSteps
	
	totalSwitches = 0
	
	bestEngine, stepSize = maxStepEngine(listEngines, listSteps)
	while stepSize != 0xFFFFFFFF:
		totalSwitches += 1
		for i in range(0, stepSize):
			listSteps.pop(0)
		#print listSteps
		bestEngine, stepSize = maxStepEngine(listEngines, listSteps)
	
	print "Result:", totalSwitches
	return totalSwitches

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
	
	numEngines = int(file.readline())	
	
	listEngines = []
	for i in range(0,numEngines):
		listEngines.append( file.readline().strip() )	
	
	numSteps = int(file.readline())
	listSteps = []	
	for i in range(0,numSteps):
		listSteps.append( file.readline().strip() )	
	
	totalResult = process(listEngines, listSteps)
	fileOut.write("Case #" + str(taskIndex+1) + ": " + str(totalResult) + "\n")
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
