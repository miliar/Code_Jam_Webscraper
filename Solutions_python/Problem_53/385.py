#!/usr/bin/python
# 2010 Qualification
''' Usage %s
'''
import logging

CurrentDebugLevel=logging.DEBUG

def ProcessCase(inFile, caseNum):
    logging.debug('Case %d', caseNum)
    param = inFile.readline().strip().split()
#    logging.debug(param)
    snapperNum = int(param[0])
    snapTimes = int(param[1])
    
    cycle = 2 ** snapperNum
    snapTimes %= cycle
    
    if snapTimes == cycle - 1:
        result = ['ON']
    else: result = ['OFF']
    
    return result

def OutputResult(outFile, caseNum, result):
    value = result[0]
    outFile.write("Case #{0}: {1}\n".format(caseNum, value))
    logging.debug("Case #{0}: {1}\n".format(caseNum, value))

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
    #dataSet = 'small'
    dataSet = 'large'
    #dataSet = 'test'
    #attempt = '-attempt1'
    attempt = ''

    ProcessDataFile('{0}-{1}{2}.in'.format(question, dataSet, attempt))

if __name__ == '__main__': main()