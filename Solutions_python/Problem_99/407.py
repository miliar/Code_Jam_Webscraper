
fp = open('A-small-attempt0.in', 'r')
fp2 = open('output.txt', 'w')
numCases = int(fp.readline())
#print numCases
def calculateProbMatrix(s, rightProb, alreadyTypedNum, currentProb, probabilityMatrix):
    l = len(s) + 1
    swrong = s + "0"
    sright = s + "1"
    currentProbRight = currentProb * rightProb[l-1]
    currentProbWrong = currentProb * (1.0 - rightProb[l-1])
    
    if(l < alreadyTypedNum):
        calculateProbMatrix(swrong, rightProb, alreadyTypedNum, currentProbWrong, probabilityMatrix)
        calculateProbMatrix(sright, rightProb, alreadyTypedNum, currentProbRight, probabilityMatrix)
    else:
        probabilityMatrix[swrong] = currentProbWrong
        probabilityMatrix[sright] = currentProbRight
for c in range(numCases):
    probabilityMatrix = {}
    inStr = fp.readline()
    inStr = inStr.split(" ")
    alreadyTypedNum = int(inStr[0])
    totalCharNum = int(inStr[1])
    rightProbStr = fp.readline()
    rightProbStr = rightProbStr.split(" ")
    rightProb = []
    for s in rightProbStr:
        rightProb.append(float(s))
    #print alreadyTypedNum, totalCharNum, rightProb
    calculateProbMatrix("", rightProb, alreadyTypedNum, 1, probabilityMatrix)  
    #calculate keep typing
    keepTypingExpected = 0
    
    for prob in probabilityMatrix:
        if(len(prob) == alreadyTypedNum):
            if(prob.find('0') == -1):
                keepTypingExpected += probabilityMatrix[prob] * float(totalCharNum + 1 - alreadyTypedNum)
            else:
                keepTypingExpected += probabilityMatrix[prob] * float(totalCharNum + 1 - alreadyTypedNum + totalCharNum + 1)
    #print keepTypingExpected
    #calculate immediate enter
    immediateEnterExpected = (totalCharNum + 2)
    backSpace = []
    backSpace.append(keepTypingExpected)
    for numBackSpace in range(1,(alreadyTypedNum+1)):
        currentExpected = 0
        for prob in probabilityMatrix:
            a = []
            for i in range(totalCharNum):
                if(i < alreadyTypedNum - numBackSpace):
                    a.append(prob[i])
            s = "".join(a)
            if(prob[:alreadyTypedNum - numBackSpace] == s):
                if(s.find('0') == -1):
                    currentExpected += probabilityMatrix[prob] * float(numBackSpace + totalCharNum - (alreadyTypedNum - numBackSpace) + 1)
                else:
                    currentExpected += probabilityMatrix[prob] * float(numBackSpace + totalCharNum - (alreadyTypedNum - numBackSpace) + totalCharNum + 1 + 1)
                #print numBackSpace, s.find('0') == -1, s, prob, probabilityMatrix[prob], float(numBackSpace + totalCharNum - (alreadyTypedNum - numBackSpace)), probabilityMatrix[prob] , float(numBackSpace + totalCharNum - (alreadyTypedNum - numBackSpace) + totalCharNum + 1)
        backSpace.append(currentExpected)
        #print ""
    
    backSpace.append(immediateEnterExpected)
    lowest = 9999999999999999
    for i in backSpace:
        if i < lowest:
            lowest = i
    fp2.write("Case #"+str(c+1)+": " + str(lowest)+"\n")
    print "Case #"+str(c+1)+": " + str(lowest)+"\n"

    
fp.close()
fp2.close()
