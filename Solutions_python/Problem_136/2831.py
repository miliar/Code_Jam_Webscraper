import math

f = open('B-large.in', 'r')

# read first line, number of trials
trials = int(f.readline())
for i in range(trials):
    cookieList = [float(x) for x in f.readline().strip().split()]

    #computed value to stop at (i = floor(X/C - 2/F - 1)), C F X
    R = 2.0
    C = cookieList[0]
    F = cookieList[1]
    X = cookieList[2]
    stop = max(0.0, math.floor(X/C - R/F - 1))

    time = 0.0
    farms = 0
    while (True):
        #print "time", time
        #print "farms", farms
        #print "    value", C / (R + farms * F)
        timeToFinishNow = X / (R + farms * F)
        timeToNextFarm = C / (R + farms * F)
        timeToFinishNext = X / (R + (farms + 1) * F)
        if (timeToFinishNow <= timeToNextFarm + timeToFinishNext):
            time += timeToFinishNow
            break
        time += timeToNextFarm
        farms += 1
    print "Case #%i: %0.7f" %(i + 1, time)