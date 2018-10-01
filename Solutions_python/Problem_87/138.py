def WalkwaysToTimeArray(totaldistance, walkingspeed, runningspeed, walkways):
    timearray = [[float(totaldistance), float(walkingspeed), float(runningspeed)]]
    for w in walkways:
        timearray[0][0] -= w[1] - w[0]
        timearray += [[float(w[1] - w[0]), float(walkingspeed + w[2]), float(runningspeed + w[2])]]
    return timearray

def AssignRunningTime(timearrayi, runningtime):
    timearray = timearrayi[:]
    # while there is running time remaining, assign it to the the place where it will make the most difference
    while runningtime > 0 and CanBeImproved(timearray):
        # find the best place to assign runningtime
        best = 0
        bestratio = float(timearray[0][1]) / timearray[0][2]
        for i in range(len(timearray)):
            if float(timearray[i][1]) / timearray[i][2] < bestratio:
                bestratio = float(timearray[i][1]) / timearray[i][2]
                best = i
        # if we have enough running time to run the whole distance, then assign this running time
        if timearray[best][0] <= runningtime * timearray[best][2]:
            runningtime -= float(timearray[best][0]) / timearray[best][2]
            timearray[best][1] = timearray[best][2]
        else:
            # determine how far we can run and then run that distance
            timearray[best][0] -= runningtime * timearray[best][2]
            timearray += [[runningtime * timearray[best][2], timearray[best][2], timearray[best][2]]]
            runningtime = 0
    return timearray

def CanBeImproved(timearray):
    result = False
    for t in timearray:
        if t[1] < t[2]:
            result = True
    return result

def SumTime(timearray):
    result = 0.0
    for t in timearray:
        result += t[0] / t[1]
    return result

#print SumTime(AssignRunningTime(WalkwaysToTimeArray(10, 1, 4, [[4, 6, 1], [6, 9, 2]]), 1.0))
#print SumTime(AssignRunningTime(WalkwaysToTimeArray(12, 1, 2, [[6, 12, 1]]), 4.0))
#print SumTime(AssignRunningTime(WalkwaysToTimeArray(20, 1, 3, [[0, 4, 5], [4, 8, 4], [8, 12, 3], [12, 16, 2], [16, 20, 1]]), 20.0))

f = file("input.txt", "r")
lines = f.readlines()
testcases = int(lines[0])
line = 0
for testcase in xrange(1, testcases + 1):
    line += 1
    indata = [int(i) for i in lines[line].split(" ")]
    inwalks = []
    for i in range(indata[4]):
        line += 1
        inwalks += [[int(j) for j in lines[line].split(" ")]]
    print "Case #" + str(testcase) + ": " + str(SumTime(AssignRunningTime(WalkwaysToTimeArray(indata[0], indata[1], indata[2], inwalks), indata[3])))
