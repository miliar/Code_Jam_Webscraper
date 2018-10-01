NA = 0
NB = 0
AToB = []
BToA = []
numA = 0
numB = 0
poolA = []
poolB = []
turnaround = 0

def solve():
    input = open("C:\\B-large.in", "r")
    output = open("C:\\Output.txt", "w")
    tests = int(input.readline())
    global AToB
    global BToA
    global numA
    global numB
    global poolA
    global poolB    
    for i in xrange(tests):
        AToB = []
        BToA = []
        numA = 0
        numB = 0
        poolA = []
        poolB = []
        readInput(input)
        processInput(output)
        output.write("Case #" + str(i + 1) + ": " + str(numA) + " " + str(numB) + "\n")        
    input.close()
    output.close()
    
def readInput(input):
    global turnaround
    turnaround = int(input.readline())
    line = input.readline()
    global NA
    global NB
    global AToB
    global BToA
    [NA, NB] = line.split(" ")
    for i in xrange(int(NA)):
        trip = input.readline().strip()
        [departure, arrival] = trip.split(" ")
        AToB += [(departure, arrival)]
    for j in xrange(int(NB)):
        trip = input.readline().strip()
        [departure, arrival] = trip.split(" ")
        BToA += [(departure, arrival)]
    AToB.sort()
    BToA.sort()

def addTurnaround(Min):
    global turnaround
    [strH, strMin] = Min[1].split(":")
    h = int(strH)
    min = int(strMin)
    min += turnaround
    h += min / 60
    min %= 60
    strMinPlusTurnaround = "%02d:%02d" % (h, min)
    return strMinPlusTurnaround

def intersect():
    pass

def processInput(output):
    global NA
    global NB
    global AToB
    global BToA
    global numA
    global numB
    global poolA
    global poolB
    for i in xrange(int(NA) + int(NB)):
        if (len(AToB) > 0) and (len(BToA) > 0):
            if AToB[0] < BToA[0]:
                Min = AToB.pop(0)
                poolB += [addTurnaround(Min)]
                if len(poolA) > 0:
                    poolA.sort()
                    if(poolA[0] <= Min[0]):
                        poolA.pop(0)
                    else:
                        numA += 1
                else:
                    numA += 1
            else:
                Min = BToA.pop(0)
                poolA += [addTurnaround(Min)]
                if len(poolB) > 0:
                    poolB.sort()
                    if(poolB[0] <= Min[0]):
                        poolB.pop(0)
                    else:
                        numB += 1
                else:
                    numB += 1
        elif len(AToB) > 0:
            Min = AToB.pop(0)         
            poolB += [addTurnaround(Min)]
            if len(poolA) > 0:
                poolA.sort()
                if(poolA[0] <= Min[0]):
                    poolA.pop(0)
                else:
                    numA += 1
            else:
                numA += 1
        else:
            Min = BToA.pop(0)
            poolA += [addTurnaround(Min)]
            if len(poolB) > 0:
                poolB.sort()
                if(poolB[0] <= Min[0]):
                    poolB.pop(0)
                else:
                    numB += 1
            else:
                numB += 1

solve()
