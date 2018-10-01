#!/usr/bin/python
# 2011 Round1A
''' Usage %s
'''
import logging
import fractions

CurrentDebugLevel=logging.DEBUG

def ProcessCase(inFile, caseNum):
    logging.debug('Case %d', caseNum)
    param = inFile.readline().strip().split()
    logging.debug(param)
    
    N = int(param[0])
    Pd = int(param[1])
    Pg = int(param[2])
    
    gcd1 = fractions.gcd(100, Pd)
    if Pd % gcd1 != 0: return [False]
    D = Pd / gcd1
    DT = 100 / gcd1

    gcd2 = fractions.gcd(100, Pg)
    if Pg % gcd2 != 0: return [False]
    G = Pg / gcd2
    GT = 100 / gcd2

    logging.debug('{}/{}, {}/{}'.format(D, DT, G, GT))
    
    if DT > N: return [False]
    if D > DT: return [False]
    

    if G < D: return [False]
    if G > GT: return [False]
    
    if DT > GT: return [False] 
    if Pd == 0 and Pg == 100: return [False]
    if Pd > 0 and Pg == 0: return [False]
    
    result = [True]
    
    return result

def OutputResult(outFile, caseNum, result):
    value = 'Possible'
    if not result[0]: value = 'Broken' 
    outFile.write("Case #{}: {}\n".format(caseNum, value))
    logging.debug("Case #{}: {}\n".format(caseNum, value))

def ProcessDataFile(fileName):
    inFile = open(fileName, 'r')
    line = inFile.readline()
    lineCount = int(line)
    outFile = open(fileName + '.out.txt', 'w')
    for i in range(1, lineCount + 1):
        result = ProcessCase(inFile, i)
        OutputResult(outFile, i, result)
    outFile.close()

def main():
    logging.basicConfig(level=CurrentDebugLevel, datefmt='%Y.%m.%d %H:%M:%S', format='%(asctime)s %(levelname)-5s %(message)s')
    question = 'A'
    dataSet = 1
    attemptCount = 2   
    isPractice = False
    
    partName = '-practice'
    dataSetNames = ['test', 'small', 'large']
    if dataSet == 0:
        dataFileName = '{0}-{1}.txt'.format(question, dataSetNames[dataSet])
    elif dataSet == 1:
        if not isPractice: partName = '-attempt{}'.format(attemptCount)
        dataFileName = '{0}-{1}{2}.in'.format(question, dataSetNames[dataSet], partName)
    else:
        if not isPractice: partName = ''
        dataFileName = '{0}-{1}{2}.in'.format(question, dataSetNames[dataSet], partName)

    ProcessDataFile(dataFileName)

if __name__ == '__main__': main()