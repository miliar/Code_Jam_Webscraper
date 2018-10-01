import sys, os
import os.path


def decode(filename):
	f = open(filename, 'r')
	base = f.readlines()
	base = base[1:] #Remove received number, we really don't need it
	for i in range(len(base)):
		base[i] = base[i].replace("\n", "") #Line feed
		base[i] = base[i].replace("\r", "") #Carrier return
		testCase = base[i].split()
		numGooglers = int(testCase[0])
		surprises = int(testCase[1])
		minimum = int(testCase[2])
		numbers = testCase[3:]
		total = 0
		for j in range(len(numbers)):
			lit = int(numbers[j])
			upperLimit = 3*minimum - 2 #From this number forwards, qualifies w/ no surprise
			lowerLimit = 3*minimum - 4 #Absolute minimum, needs surprise
			if(upperLimit < 0):
				upperLimit = minimum
			if(lowerLimit < 0):
				lowerLimit = minimum
			if  (lit >= upperLimit):
				total+=1
			elif(lit >= lowerLimit and surprises != 0):
				total+=1
				surprises-=1
		base[i] = "Case #" + str(i+1) + ": "+ str(total)
	r = open("Results.txt", "w")
	for line in base:
		r.write("%s\n" % line)
	f.close()
	r.close()
	
if __name__ == "__main__":
	filename = sys.argv[1]
	decode(filename)