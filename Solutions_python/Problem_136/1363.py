
def timeWaitTo(currentCookies, production, limit):
    return (limit-currentCookies)/float(production)

def getTime(currentTime, currentCookies, production, limit):
    return currentTime + timeWaitTo(currentCookies, production, limit)

def getBest(cost, extra, goal):
    currentTime = 0
    bestTime = 10**10
    farm = 0
    while farm>=0:
        time = getTime(currentTime,0,2+extra*farm,goal)
        timeFarm = timeWaitTo(0, 2+extra*farm,cost)
        currentTime+=timeFarm
        
        #print "With %d farms" % farm
        #print timeFarm
        #print time 
        
        if time < bestTime:
            bestTime = time
        else:
            #print "RESULT = " , bestTime
            return bestTime
        farm+=1

fInp = open('p2.inc','r')
fOut = open('p2.out','w')
inp = fInp.readline()
N = int(inp)
#print N
for i in range(N):
    C,F,X = map(float, fInp.readline().split())
    fOut.write("Case #%d: %.7f\n" % (i+1, getBest(C,F,X)) )
    
fInp.close()
fOut.close()
#print getBest(500,4,2000)