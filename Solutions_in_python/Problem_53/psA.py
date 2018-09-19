#!/usr/bin/python
import sys

POWER = 0
STATE = 1

inputFile = open(str(sys.argv[1]), 'r')
testCases = int(inputFile.readline().rstrip())
for i in range(testCases):
    line = inputFile.readline()
    num_snapper, snap_times = line.rstrip().split()
    num_snapper = int(num_snapper)
    snap_times = int(snap_times) 
    snappers = [[False, False] for count in range(0, num_snapper)]
    snappers[0][POWER] = True
    for k in range(0, snap_times): 
        for n in range(0, num_snapper):
            if snappers[n][POWER]:  
                snappers[n][STATE] = not snappers[n][STATE]
        for n in range(1, num_snapper):
            if snappers[n-1][POWER] and snappers[n-1][STATE]:
                snappers[n][POWER] = True
            else:
                snappers[n][POWER] = False
    if snappers[num_snapper-1][POWER] and snappers[num_snapper-1][STATE]:
        print 'Case #%d: ON' % (i+1)
    else:
        print 'Case #%d: OFF' % (i+1)
inputFile.close()
