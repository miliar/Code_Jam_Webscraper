from __future__ import print_function
def tidyString(number, chainNum, chainStart):
    if number[chainStart] == '1': #implies 0th index
        return '9' * (len(number) - 1)
    else:
        decreased = int(number[chainStart]) - 1
        return number[:chainStart] + str(decreased) + ('9' * (len(number)-chainStart-1))

def checkString(number):
    largest = -1
    chainStart = -1
    chainNum = -1
    for digit in xrange(len(number)):
        currentDigit = int(number[digit])
        if currentDigit < largest:
            return tidyString(number, chainNum, chainStart)
        else:
            largest = currentDigit
            if currentDigit != chainNum:
                chainStart = digit
                chainNum = currentDigit
    return number #number already tidy


f = open("B-large.in",'r')
output = open("output.txt",'w')
testCases = int(f.readline().strip())
for x in xrange(1, testCases+1):
    print ('Case #' + str(x) + ': ' + checkString(f.readline().strip()), file=output)
