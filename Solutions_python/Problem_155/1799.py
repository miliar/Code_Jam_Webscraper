import sys

def standingOvation(audience, shyness):
    totalAud = shyness
    for shyVal in range(len(audience)):
        totalAud=totalAud+int(audience[shyVal])
        if totalAud-1 < shyVal:
            ##print "Shy Level:%d Audience Members:%d" %(shyVal,totalAud)
            return False
        ##print "Shy Level:%d Audience Members:%d" %(shyVal,totalAud)
    return True

def optimalCaseReport(caseNo, members):
    myfile = open("standingOvationLarge.txt","a")
    myfile.write("Case #%d: %d\n" %(caseNo, members))
    ##print "Case #%d: %d" %(caseNo, members)

def importFile(impFile):
    numCases=int(impFile.readline())
    ##print numCases
    a=[]
    for i in range(0,numCases):
        a.append(impFile.readline().rstrip().split(" "))
    ##print a
    return a
    
impFile = open("A-large.in","r")
audience=importFile(impFile)

sMax = 6
mArray=len(audience)
##print mArray

audArray=[]
for i in range(0,mArray):
    audArray=audience[i][1]
    ##print audArray
    optimal=False
    shyness = -1
    while optimal==False:
        shyness=shyness+1
        optimal=standingOvation(audArray, shyness)

    optimalCaseReport(i+1, shyness)

