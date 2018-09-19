import sys
from os.path import expanduser

currentProblem = 'A' #A/B/C/D
smallAttemptNo = 0
largeAttempt = True
debug = True

def solveA(ipfile):
    n = int(ipfile.readline())
    data = [int(x) for x in ipfile.readline().split(' ')]
    prev = data[0]
    
    maxEaten = getMaxEaten(data)
    
    case1 = 0
    case2 = 0
    for i in range(1,len(data)):
        curr = data[i]
        diff = curr - prev
        if(diff < 0):
            case1 += abs(diff)
            
        if(maxEaten>0):
            case2 += min (prev,maxEaten)
            #print case2,maxEaten,prev,diff,min (prev,maxEaten)
        prev = curr

    return str(case1)+" "+str(case2)
        
    
def getMaxEaten(data):
    maxEaten = -1-sys.maxint
    prev = data[0]
    for i in range(1,len(data)):
        if(-data[i]+prev > 0):
            maxEaten = max(maxEaten,-data[i]+prev)
        prev = data[i]
        
    return maxEaten
    
def solveB(ipfile):
    pass

def solveC(ipfile):
    pass

def solveD(ipfile):
    pass

if __name__ == "__main__":
    ipFilePath = expanduser('~') + (('/Downloads/{0}-small-attempt{1}.in'.format(currentProblem, smallAttemptNo) if not largeAttempt else '/Downloads/{0}-large.in'.format(currentProblem)))
    opFilePath = expanduser('~') + ('/Downloads/output.out')
    filestring = ''
    
    problemFunctionMap = {
        'A' : solveA,
        'B' : solveB,
        'C' : solveC,
        'D' : solveD
    }

    with open(ipFilePath,'r') as ipfile, open(opFilePath, 'w') as opfile:
        
        cases = int(ipfile.readline())
        for case in range(1,cases+1):
            
            result = problemFunctionMap[currentProblem](ipfile)
            caseResultString = 'Case #{0}: {1}\n'.format(case,result) 
            opfile.write(caseResultString)
            
            if(debug):
                print caseResultString,

    print filestring
