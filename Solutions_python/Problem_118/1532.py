import math
import random
import time

def isPalindrome(s):
    if len(s) < 2:
        return True
    else:
        return s[0]==s[-1] and isPalindrome(s[1:-1])

def buildCumulativeTable():
    table = {0:0}
    count = 0
    square = 1
    limit = pow(10,14)

    while square <= limit:
        root = int(math.sqrt(square))
        if isPalindrome(str(square)):
            if isPalindrome(str(root)):
                count += 1
                table[square] = count
        square = pow(root+1,2)
    return table

def lessThan(z, sortedList):
    theta = 0
    for item in sortedList:
        if item <= z:
            theta = item
    return theta

def inBetween(a,b):
    return table[lessThan(b,sortedList)] - table[lessThan(a-1,sortedList)]


#start_time = time.time()
table = buildCumulativeTable()
sortedList = table.keys()
sortedList.sort()
#print 'Table and List done by: ', time.time() - start_time, "seconds"

fileIn = open('C-large-1.in', 'r')
fileOut = open('c-small-output.out','w')

cases = int(fileIn.readline()[:-1])

for case in range(1,cases+1):
    aAndb = fileIn.readline()[:-1].split()
    a = int(aAndb[0])
    b = int(aAndb[1])
    output =  "Case #%r: %r\n" %(case, inBetween(a,b))
    fileOut.write(output)



fileIn.close()
fileOut.close()
#print 'Done by: ', time.time() - start_time, "seconds"