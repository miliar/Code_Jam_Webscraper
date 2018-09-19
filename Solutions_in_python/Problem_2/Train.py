from compiler.ast import Compare
def CompareTime(timeA, timeB):
    if int(timeA[0:2]) > int(timeB[0:2]):return 1
    elif int(timeA[0:2]) < int(timeB[0:2]):return -1
    elif int(timeA[3:5]) > int(timeB[3:5]):return 1
    elif int(timeA[3:5]) < int(timeB[3:5]):return -1
    else: return 0

def AddTime(inTime, turnaroundTime):
    newTime = inTime[6:]
    hour = int(newTime[0:2])
    minute = int(newTime[3:])
    minute += turnaroundTime
    if minute >= 60:
        minute %= 60
        hour += 1
    newTime = '%.2d:%.2d' % (hour, minute)
    return newTime

def FindFirst(timeList):
    minTime = ['', 0]
    for i in range(len(timeList)):
        eachTime = timeList[i]
        if minTime[0] == '' or \
        CompareTime(minTime[0], eachTime) >= 0:
            minTime[0] = eachTime
            minTime[1] = i
    return minTime

if __name__ == '__main__':
    inFile = open('B-large.in')
    inLines = inFile.readlines()
    inFile.close()
    numCases = int(inLines[0].strip())
    index = 1
    #print numCases
    for iCase in range(numCases):
        # index is case definition
        turnaroundTime = int(inLines[index])
        numA = int(inLines[index + 1].split(' ')[0])
        numB = int(inLines[index + 1].split(' ')[1])
        
        timeA = [x.strip() for x in inLines[index + 2:index+2+numA]]
        timeB = [x.strip() for x in inLines[index + numA + 2:index+2+numB + numA]]
        
        startA, startB = (0,0)
        trainListA, trainListB = list(), list()
        
        while True:
            gotA, gotB = None, None
            AToGo = False
            BToGo = False
            if len(timeA) > 0:
                gotA = FindFirst(timeA)
                if len(timeB) > 0:
                    gotB = FindFirst(timeB)
                    if CompareTime(gotA[0], gotB[0]) > 0:
                        BToGo = True
                    elif CompareTime(gotA[0], gotB[0]) == 0:
                        if len(trainListA) > 0:
                            AToGo = True
                        else:
                            BToGo = True
                    else: AToGo = True
                    
                else: AToGo = True
            else:
                if len(timeB) > 0:
                    gotB = FindFirst(timeB)
                    BToGo = True
                else: break
            
            #print AToGo, BToGo
            #print gotA, gotB
            if AToGo:
                timeA.pop(gotA[1])
                #Find in the train list
                foundA = False
                for eachTrain in trainListA:
                    if CompareTime(gotA[0], eachTrain) >= 0:
                        foundA = True
                if not foundA:
                    startA += 1
                else:
                    trainListA.pop(0)
                    #remove
                trainListB.append(AddTime(gotA[0], turnaroundTime))
                trainListB.sort(CompareTime)
                #print gotA
            elif BToGo:
                timeB.pop(gotB[1])
                #Find in the train list
                foundB = False
                #print trainListB
                for eachTrain in trainListB:
                    if CompareTime(gotB[0], eachTrain) >= 0:
                        foundB = True
                if not foundB:
                    startB += 1
                else:
                    trainListB.pop(0)
                    #remove
                trainListA.append(AddTime(gotB[0], turnaroundTime))
                trainListA.sort(CompareTime)
                #print gotB

#            for eachTrain in trainListA:
#                print eachTrain
#                if CompareTime(gotA[0], eachTrain) >= 0:
#                    foundA = True
#            if foundA: trainListA.pop(0)
            #print timeA
            #timeA.pop(gotA[1])
#            if len(timeA) == 0 and len(timeB) == 0:
#                break
        
        #print FindFirst(timeA)
        #print FindFirst(timeB)
        
        print 'Case #%d: %d %d' % (iCase + 1, startA, startB)        
        ##
        index += numA + numB + 2
        