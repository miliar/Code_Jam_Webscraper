import sys

class robot():
    def __init__(self, currPos, idleTime):
        self.currPos = currPos
        self.idleTime = idleTime
    
    def setCurrPos(self, cP):
        self.currPos = cP
    
    def addToIdle(self, idle):
        self.idleTime += idle
    
    def resetIdle(self):
        self.idleTime = 0

def sub(n1, n2):
    return 0 if n2 > n1 else n1 - n2

def processLine(line):
    
    inputSeq = line.split()
    inputSeq.reverse()
    
    seqLen = int(inputSeq.pop())
    #print 'seqLen', str(seqLen)
    #print 'inSeq', str(inputSeq)
    
    pushTime = 1
    
    # sample input
    
    Orng = robot(1, 0)
    Blue = robot(1, 0)
    
    totalTime = 0
    
    for i in range(seqLen):
        # next action
        botID = inputSeq.pop()
        target = int(inputSeq.pop())
        botID, target
        
        # foreground
        fgBot = Orng if botID == 'O' else Blue
        # background
        bgBot = Orng if botID == 'B' else Blue
        
        #if fgBot is Orng: print "Orange to move"
        #else: print "Blue to move"
        
        dist = abs(target - fgBot.currPos)
        timeBforePush = sub(dist, fgBot.idleTime)
        #print "idle was", str(fgBot.idleTime)
        fgBot.resetIdle()
        actionTime = timeBforePush + pushTime
        fgBot.setCurrPos(target)
        #print "net action time:", str(actionTime)
        bgBot.addToIdle(actionTime)
        totalTime += actionTime
        
    return totalTime

filename = sys.argv[1]
f = open(filename, 'r')
tCases = int(f.readline().strip())

outFile = open('out.txt', 'w')

for i in range(tCases):
    li = f.readline().strip()
    t = processLine(li)
    outFile.write('Case #' + str(i+1) + ': ' + str(t) + '\n')

outFile.close()
    
