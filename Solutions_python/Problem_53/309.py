'''
Created on 08.05.2010

@author: Dong Li
'''

def getOutput(N,K):
    statues=[]
    for i in range(N):
        statues.append((OFF,noPower))
    statues[0]=(OFF,hasPower)
    for i in range(K):
        count=0
        for (isOn,withPower) in statues:
            if withPower==hasPower:
                statues[count]=(-isOn,hasPower)
            count+=1
        count=0
        allOff=False
        for (isOn,withPower) in statues:
            if withPower==hasPower and isOn==OFF and not allOff:
                allOff=True
            elif allOff:
                statues[count]=(isOn,noPower)
            elif withPower==hasPower and isOn==ON and (count+1)<N:
                statues[count+1]=(statues[count+1][0],hasPower)
            count+=1
    print statues
    if statues[N-1]==(ON,hasPower):
        return "ON"
    else:
        return "OFF"


OFF=-1
ON=1
hasPower=1
noPower=-1
caseNum=0
inputTuples=[]
inputFile="A-small-attempt1.in"
outputFile=open("A-small-attempt0.out",'w')
input=open(inputFile)
counter=0
for line in input:
    if counter==0:
        caseNum=int(line)
        counter+=1
    else:
        inputTuples.append(line.split())
        counter+=1
for i in range(caseNum):
    result="Case #"+str(i+1)+": "+getOutput(int(inputTuples[i][0]),int(inputTuples[i][1]))
    outputFile.write(result+"\n")
    print result











