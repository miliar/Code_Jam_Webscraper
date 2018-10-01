def testPalindromeNumber(number):

    if number != int(number):
        return False

    workingNumber = int(number)
    reversedNumber = 0

    while (workingNumber > 0):
        reversedNumber = reversedNumber * 10 + workingNumber % 10
        workingNumber = workingNumber / 10

    if reversedNumber == number:
        return True
    else:
        return False

import math

f = open('C-small-attempt0.in.txt', 'rU')

numberOfCases = int(f.readline())
i = 0
outputString = '';

while i < numberOfCases:
    count = 0
    testCase = f.readline().rstrip()
    lowerBound = int((testCase.split())[0])
    upperBound = int((testCase.split())[1])

    for j in xrange(lowerBound, upperBound + 1):
        if testPalindromeNumber(j):
            if testPalindromeNumber(math.sqrt(j)):
                print j
                count = count + 1

    print "----"
    outputString += "Case #" + str(i + 1) + ": " + str(count) + "\n"

    i = i + 1

f.close()

fo = open("output.txt","w")
fo.write(outputString[:-1])
fo.close()