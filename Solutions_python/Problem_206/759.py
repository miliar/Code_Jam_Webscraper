import numpy as np
import time

def readInputFile(fnamein):
    with open(fnamein) as f:
        content = f.readlines()
    content = [x.strip() for x in content] 
    return content

def writeOutputFile(fnameout,outlist):        
    # Write to file
    with open(fnameout, "w") as output:
        for item in outlist:
            output.write("%s\n" % item)

def TimeUntilArrival(D,K,S):
    return (D-K)/(S*1.0)

def findLatestArrival(D,horselist):
    latest = 0.0
    for i in np.arange(0,len(horselist)):
        temp_input = horselist[i].split(' ')
        temp_K, temp_S = int(temp_input[0]), int(temp_input[1])
        temp_arrival = TimeUntilArrival(D,temp_K,temp_S)
        if temp_arrival>latest:
            latest = temp_arrival
    return latest

def findMaxSpeed(D,horselist):
    latestArrival = findLatestArrival(D,horselist)
    maxspeed = D/latestArrival
    return(maxspeed)

def solveA(fnamein,fnameout):
    inputlist = readInputFile(fnamein)
    outputlist = list()
    T = int(inputlist[0])
    index = 1
    for i in np.arange(1,T+1):
        temp_input = inputlist[index].split(' ')
        temp_D, temp_N = int(temp_input[0]), int(temp_input[1])
        temp_horselist = inputlist[(index+1):(index+temp_N+1)]
        temp_maxSpeed = findMaxSpeed(temp_D,temp_horselist) 
        outputlist.append('Case #'+str(i)+': '+str(temp_maxSpeed))
        index = index+temp_N+1
    writeOutputFile(fnameout,outputlist)
    
tic = time.clock()
solveA('A-large.in','A-large-output.txt')
toc = time.clock()
print('Runtime: '+str(toc - tic)+'sec')    