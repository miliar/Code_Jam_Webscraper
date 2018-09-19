from math import fabs

path = "A-large.in"

allTests = []
results  = []

inFile = open(path)
inFile.readline()

print "--------------------------"
print "--------------------------"
print "--------------------------"
print "--------------------------"
print "--------------------------"
print "--------------------------"
print "--------------------------"
print "--------------------------"


for line in inFile:

	testCases = []

	line = line.rstrip("\n")
	tasks = line.split(" ")
	
	testButtons = int(tasks[0])

	if tasks > 0:
		for i in range(1,len(tasks),2):
			testCases.append((tasks[i],int(tasks[i+1])))

	allTests.append(testCases)
	
for test in allTests:
	print
	print test

	totalTime = 0

	position = {}
	position["B"] = 1
	position["O"] = 1

	timeAtLastMove = {}
	timeAtLastMove["B"] = 0
	timeAtLastMove["O"] = 0


	printout = {}
	printout["B"] = []
	printout["O"] = [] 


	for movement in test:
		bot 		= movement[0]

		destination 	= movement[1]
		distance	= int(fabs(position[bot] - destination))
		reqdTime	= distance + 1
		

		print bot + " --> " + str(destination),
		print "("+str(reqdTime)+") ",

		changeInTime = reqdTime - (totalTime - timeAtLastMove[bot])
		if changeInTime < 1:
			changeInTime = 1
###############
		pos = position[bot]
		t = totalTime+changeInTime-len(printout[bot])
		if pos < destination:
			inc = 1
		else:
			inc = -1
		while not pos == destination:
			printout[bot].append("Move to button "+str(pos+inc))
			pos += inc
			t = t -1
		while t > 1:
			printout[bot].append("Stay at button "+str(pos))
			t = t -1
			
		printout[bot].append("Push button "+str(pos))
		
#################
		totalTime += changeInTime
		

		timeAtLastMove[bot] = totalTime

		print " [" +str(totalTime)+"] ", str(changeInTime)
	
		position[bot] = destination

	print "Time | Orange            | Blue"
	print "-----+-------------------+-----------------"
	for i in range(0,totalTime):
		print str(i+1).center(5) + "|",
		try:
			print  printout["O"][i].center(18)+"|",
		except:
			print "                  |",
		try:
			print printout["B"][i].center(18)
		except:
			print


		

        results.append(totalTime)


outFile = open("output.txt", 'w')

for i in range(0,len(results)):
	outFile.write("Case #" + str(i+1) + ": " + str(results[i]) + "\n")

outFile.close()


		
