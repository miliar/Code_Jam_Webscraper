#!/usr/bin/python2.5

#fileNameInput  = 'B-small.in'
#fileNameOutput = 'B-small.out'
fileNameInput  = 'B-large.in'
fileNameOutput = 'B-large.out'


def findMinimumTime(list1, list2):
    min1 = None
    min2 = None
    if len(list1) == 0:
        min1 = None
    else: min1 = list1[0]
    if len(list2) == 0:
        min2 = None
    else: min2 = list2[0]
    if min1 == None and min2 == None: return (None, None)
    if min1 != None and min2 != None:
        if list1[0] > list2[0]:
            min = list2[0]
            w = 1
        else:
            min = list1[0]
            w = 0
    elif min1 == None:
        min = list2[0]
        w = 1
    else:
        min = list1[0]
        w = 0
    return (w, min)

def nextStation(currStation):
    if currStation == 0: return 1
    else: return 0

def findDep(d, time):
    res = None
    for x in d[::-1]:
        if x >= time: res = x
    if res==None: return None
    else: return d.index(res)

def findSolution(T, trains1, trains2):
    trains = [None, None]
    trains[0] = trains1
    trains[1] = trains2
    newTrains = [0, 0]
    deps = [[], []]
    for x in trains1:
        deps[0].append(x[0])
    for x in trains2:
        deps[1].append(x[0])
    deps[0].sort()
    deps[1].sort()
    trains[0].sort(lambda x,y: cmp(x[0],y[0]))
    trains[1].sort(lambda x,y: cmp(x[0],y[0]))
    while len(deps[0]) + len(deps[1]) > 0:
        station, time = findMinimumTime(deps[0], deps[1])
        newTrains[station] += 1                 # create a train
        deps[station] = deps[station][1:]       # remove one position from dep
        newTime = trains[station][0][1] + T     # time = when it arrives + T
        trains[station] = trains[station][1:]   # remove one position from trains
        while True:
            station = nextStation(station)      # --->
            if len(deps[station]) == 0 or deps[station][-1] < newTime: break # check the latest time
            chDep = findDep(deps[station], newTime)
            del deps[station][chDep]                 # remove one position from dep
            newTime = trains[station][chDep][1] + T  # time = when it arrives + T
            del trains[station][chDep]               # remove one position from trains
            #deps[station] = deps[station][1:]       # remove one position from dep
            #newTime = trains[station][0][1] + T     # time = when it arrives + T
            #trains[station] = trains[station][1:]   # remove one position from trains
    return (newTrains[0], newTrains[1])

if __name__ == '__main__':
    input = file(fileNameInput, 'r').readlines()
    output = file(fileNameOutput, 'w')

    # filter \n charachters
    for x in xrange(len(input)):
        input[x] = input[x].replace('\r','').replace('\n','')

    numberOfTests = int(input[0])
    line = 1
    for x in xrange(1, numberOfTests+1):
        T = int(input[line])
        trains = input[line+1].split()
        t1 = int(trains[0])
        t2 = int(trains[1])
        line += 2
        trains1 = []
        trains2 = []
        for a in xrange(t1):
            hours = input[line].split()
            line += 1
            tDe = hours[0].split(':')
            tAr = hours[1].split(':')
            minDe = int(tDe[0])*60 + int(tDe[1])
            minAr = int(tAr[0])*60 + int(tAr[1])
            trains1.append([minDe, minAr])
        for a in xrange(t2):
            hours = input[line].split()
            line += 1
            tDe = hours[0].split(':')
            tAr = hours[1].split(':')
            minDe = int(tDe[0])*60 + int(tDe[1])
            minAr = int(tAr[0])*60 + int(tAr[1])
            trains2.append([minDe, minAr])
        solution = findSolution(T, trains1, trains2)
        output.write('Case #' + str(x) + ': ' + str(solution[0]) + ' ' + str(solution[1]) + '\n')
    output.close()
    print 'done'
