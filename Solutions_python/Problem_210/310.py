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

def makeArrays(Alist):
    starts, stops = [], []
    for i in np.arange(0,len(Alist)):
        temp_input = Alist[i].split(' ')
        starts.append(int(temp_input[0]))
        stops.append(int(temp_input[1]))
    return starts, stops


def minChanges(Aclist, Ajlist):
    if (not Aclist and len(Ajlist)==1) or (not Ajlist and len(Aclist)==1) or (len(Aclist)==1 and len(Ajlist)==1):
        min_changes = 2
    else: # one has 2 activities, the other 0
        if not Ajlist:
            Alist = Aclist
        else:
            Alist = Ajlist    
        starts, stops = makeArrays(Alist)
        if (np.max(stops)-np.min(starts))<=720 or (np.max(starts)-np.min(stops))>=720:
            min_changes = 2
        else:
            min_changes = 4
    return min_changes
    
def solveB(fnamein,fnameout):
    inputlist = readInputFile(fnamein)
    outputlist = list()
    T = int(inputlist[0])
    index = 1
    for i in np.arange(1,T+1):
        temp_input = inputlist[index].split(' ')
        temp_Ac, temp_Aj = int(temp_input[0]), int(temp_input[1])
        temp_Aclist = inputlist[(index+1):(index+temp_Ac+1)]
        temp_Ajlist = inputlist[(index+temp_Ac+1):(index+temp_Ac+temp_Aj+1)]
        temp_minChanges = minChanges(temp_Aclist,temp_Ajlist) 
        outputlist.append('Case #'+str(i)+': '+str(temp_minChanges))
        index = index+temp_Ac+temp_Aj+1
    writeOutputFile(fnameout,outputlist)           
	
tic = time.clock()
solveB('B-small-attempt4.in','B-small-output.txt')
toc = time.clock()
print('Runtime: '+str(toc - tic)+'sec')