sample    = 'sample.txt'
smallData = 'A-small-attempt0.in'
largeData = 'A-large.in'
output    = 'output.txt'

def getMinOpt(sizeOfAsMote, moteList):
##    print('moteList =', moteList)
    
    if moteList == ():
        return 0

    newSizeOfAsMote = sizeOfAsMote
    newMoteList = moteList
##    optNum = 0
    
    while (newSizeOfAsMote > newMoteList[0]):
##        print('newMoteList =', newMoteList)
        
        newSizeOfAsMote += newMoteList[0]
##        print('newSizeOfAsMote =', newSizeOfAsMote)
        newMoteList = newMoteList[1:]
##        print('newMoteList after =', newMoteList)

##        print(newSizeOfAsMote, '>', newMoteList[0], newSizeOfAsMote > newMoteList[0])

        if newMoteList == ():
            return 0

    # add a mote
    if newSizeOfAsMote > 1:
        newMoteList1 = (newSizeOfAsMote - 1,) + newMoteList
        optNum1 = 1 + getMinOpt(newSizeOfAsMote, newMoteList1)
    else:
        import sys
        optNum1 = sys.maxsize
    
    # remove a mote
    newMoteList2 = newMoteList[1:]
    optNum2 = 1 + getMinOpt(newSizeOfAsMote, newMoteList2)

    return min(optNum1, optNum2)

### Memoize

class Memoize:
    """Memoize(fn) - an instance which acts like fn but memoizes its arguments
       Will only work on functions with non-mutable arguments
    """
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

getMinOpt = Memoize(getMinOpt)

def testGetMinOpt():
##    print(getMinOpt(2, (1, 2)))
    print(getMinOpt(2, (1, 2)) == 0)
    print(getMinOpt(1, (1, 1, 1, 1)) == 4)



    print


##testGetMinOpt()

with open(largeData, 'r') as f, open(output, 'w') as outFile:
    t = int(f.readline())
##    print('T =', t)

    for caseIdx in range(t):
##        print('Index', caseIdx)
        
        a, n = map(int, f.readline().split())
##        print('A, N =', a, n)

        moteList = list(map(int, f.readline().split()))
##        print('mote list:', moteList)

        moteList.sort()
##        print('sorted mote list:', moteList)

        minOptNum = getMinOpt(a, tuple(moteList))
        outputText = 'Case #{0}: {1}\n'.format(caseIdx+1, minOptNum)
##        print(outputText)
        outFile.write(outputText)



##        print()
