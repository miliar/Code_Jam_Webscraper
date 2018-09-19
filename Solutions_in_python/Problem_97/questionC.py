import re
filename = "C-small-attempt0 (1).in"
thefile = open(filename,'r')
numOfCases = int(thefile.readline())

def findAll(number):
    recycledList = []
    for i in range(1,len(str(number))):
        recycledNum = str(number)[i:]+str(number)[:i]
        if recycledNum != number and recycledNum[0]!=0:
            recycledList.append(int(recycledNum))
    return recycledList

findCase = 0

for i in range(numOfCases):
    number1,number2 = re.findall('[0-9]+',thefile.readline())
    number1,number2 = int(number1),int(number2)
    theRange = range(number1,number2+1)
    foundCase = 0
    foundList = []
    for pair_first in theRange:
        recycledList = findAll(pair_first)
        for pair_second in recycledList:
            if pair_first<pair_second:
                if pair_second in theRange:
                    foundCase +=1
                    foundList.append((pair_first,pair_second))
                    
    print "Case #"+str(i+1)+": "+str(foundCase)

    
