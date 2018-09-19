#!/usr/bin/env python

import sys

lines = [x.strip() for x in sys.stdin.readlines()]

lines = lines[1:]

results = []

for l in lines :
    points = l.split()[1:]
    orange = []
    blue = []
    order = []
    c = None
    for i in range(len(points)) :
        if i % 2 == 0 :
            if points[i] == 'O' :
                c = orange
                order.append(0)
            else :
                c = blue
                order.append(1)
        else :
            c.append(int(points[i]))

    time = 0
    orangeDiff, blueDiff = 0, 0
    orange.reverse()
    blue.reverse()
    if len(blue) > 0 :
        blueDiff = blue[-1] - 1
    if len(orange) > 0 :
        orangeDiff = orange[-1] - 1
    for r in order :
        if r == 0 :
            time += orangeDiff + 1
            blueDiff = max(blueDiff - (orangeDiff + 1), 0)
            if len(orange) > 1 :
                orangeDiff = abs(orange[-2] - orange[-1])
            orange.pop()
        else :
            time += blueDiff + 1
            orangeDiff = max(orangeDiff - (blueDiff + 1), 0)
            if len(blue) > 1 :
                blueDiff = abs(blue[-2] - blue[-1])
            blue.pop()
    results.append(time)

for i in range(len(results)): 
    print "Case #" + str(i+1) + ": " + str(results[i])
