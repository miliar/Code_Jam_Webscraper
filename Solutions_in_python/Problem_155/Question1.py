# Tashiv Sewpersad
# Google Code Jam 2014
# Qualiification Round - Question 2

## TFile Handeling
sInFile = "input.in"
sOutFile = "output.txt"
TFile = open(sInFile,"r")

## Declarations
def getLine():
	sResult = TFile.readline()
	sResult = sResult[0:len(sResult)-1]
	return sResult

def writeOutput(sOutput):
	OutFile = open(sOutFile,"a")
	OutFile.write(sOutput+"\n")
	OutFile.close()

def makeOutputFile():
	OutFile = open(sOutFile,"w")
	OutFile.close()

## Live Code
makeOutputFile()
iTcases = eval(getLine())
for i in range(1,iTcases+1):
	sOutput = ""
	sCaseData = getLine().split()
	iMaxShyLevel = eval(sCaseData[0])
	# Special Case
	if (iMaxShyLevel == 0):
		sOutput = "Case #" + str(i) + ": 0"
		writeOutput(sOutput) 
		continue;
	# General Case
	sAudience = sCaseData[1];
	iStanding = eval(sAudience[0]); 
	iNeededFriends = 0;
	for j in range(1, iMaxShyLevel+1):
		if eval(sAudience[j]) == 0:
			continue
		if j > iStanding:
			iNeededFriends += j - iStanding
			iStanding = j + eval(sAudience[j])
		else:
			iStanding += eval(sAudience[j])
		sOutput = "Case #" + str(i) + ": " + str(iNeededFriends)
	writeOutput(sOutput)

## Final Code
TFile.close()  	
	 
	


