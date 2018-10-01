import csv as csv

print 'Starting'

inFile = open('B-large.in','rb')
##inFile = open('B-small-attempt0.in','rb')
##inFile = open('test.in','rb')
data = csv.reader(inFile,delimiter=' ')
numTests = int(data.next()[0])

outFile = open('outputSubmission.csv','wb')
outer = csv.writer(outFile)
##outString = 'Case #1:' 
##outer.writerow([outString])


def backCount(num):    
    numList = list(str(num))
    currentVal = 9
    for k in xrange(len(numList)):
        testVal = int(numList[-(j+1)])
        if testVal > currentVal:
            currentVal = testVal
            return False
    return True


count = 0
for i in xrange(numTests):
    inputNumber = data.next()[0]
    outputList = [val for val in inputNumber]
    print inputNumber
    currentVal = 9
    for j in xrange(len(inputNumber)):        
        testVal = int(inputNumber[-(j+1)])        
        #print testVal, currentVal
        if testVal > currentVal:
            outputList[-(j+1)] = str(testVal-1)
            for k in xrange(j):
                outputList[-(k+1)] = '9'
            currentVal = testVal-1
        else:
            currentVal = testVal
        #print pString
    outputNumber = ''
    for val in outputList:
        outputNumber += val
    outputNumber = outputNumber.lstrip('0')
    outString = 'Case #' + str(i+1) + ': ' + outputNumber
    #print outString
    outer.writerow([outString])
    count += 1


inFile.close()
outFile.close()
            
        

print 'Done'
