atrains=[0] * (23*60 + 59)
btrains=[0] * (23*60 + 59)

def addTrainAtTime(ab, time):
    if ab=="a":
        for x in xrange(time, 23*60 + 59):
            atrains[x] += 1
    if ab=="b":
        for x in xrange(time, 23*60 + 59):
            btrains[x] += 1    

def removeTrainAtTime(ab, time):
    fail = False
    if ab=="a":
        for x in xrange(time, 23*60 + 59):
            atrains[x] -= 1
            if atrains[x] < 0:
                fail = True
    if ab=="b":
        for x in xrange(time, 23*60 + 59):
            btrains[x] -= 1    
            if atrains[x] < 0:
                fail = True
    return fail

def timeToNumber(time):
    s = time.split(":")
    return int(s[0])*60 + int(s[1])


f = open("C:\TEST2.TXT")

lines = f.read().split("\n")

times= int(lines[0])
turnaround = int(lines[1])


lines = lines[2:]

for x in xrange(times):
    trips = lines[0].split(" ")
    tripsfroma = int(trips[0])
    tripsfromb = int(trips[1])
    lines = lines[1:]
    for a in xrange(tripsfroma):
        d = lines[a].split(" ")
        #dont forget turnaround
        removeTrainAtTime("a", timeToNumber(d[0]))
        addTrainAtTime("b", timeToNumber(d[1]) + turnaround)
    lines = lines[tripsfroma:]
    for b in xrange(tripsfromb):
        d = lines[b].split(" ")
        removeTrainAtTime("b", timeToNumber(d[0]))
        addTrainAtTime("a", timeToNumber(d[1]) + turnaround)
    
    
    while True:
        nofail = True
        for i in atrains:
            if i < 0:
                nofail = False
                addTrainAtTime("a", timeToNumber("00:00"))
        if nofail == True:
            break
    
    while True:
        nofail = True
        for i in btrains:
            if i < 0:
                nofail = False
                addTrainAtTime("b", timeToNumber("00:00"))
        if nofail == True:
            break
    
    print "Case #" + str(x+1)+": " + str(atrains[0])+ " " +   str(btrains[0])
    lines = lines[tripsfromb:]
    atrains=[0] * (23*60 + 59)
    btrains=[0] * (23*60 + 59)
    turnaround = int(lines[0])
    lines = lines[1:]
