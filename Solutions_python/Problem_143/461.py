import numpy

def importData(inputFileName):
    data = [i.strip() for i in open(inputFileName).readlines()]
    data = [x.split() for x in data]
    caseCount=int(data.pop(0)[0])   
    return data

def splitData(data):
    return data

def processCase(case):
    (a, b, k)=map(int, case)
    count=0
    for x in xrange(a):
        for y in xrange(b):
            if x&y<k:
                count +=1
    return str(count)
    

def exportOutput(inputFileName):
    cases=splitData(importData(inputFileName))
    output='\n'.join(['Case #'+str(caseID+1)+': '+processCase(case) for (caseID, case) in enumerate(cases)])
    outputFileName=inputFileName.replace('.in','-output.txt')
    f=open(outputFileName, 'wb')
    f.write('')
    f.writelines(output)
    f.close()
