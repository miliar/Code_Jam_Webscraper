#!/usr/bin/python

import sys, datetime

SEPARATE_LINE = "=" * 20

def genResult(radiuses):
    print "genResult radiuses = %s" % radiuses
    positions = [None] * len(radiuses)
    for radius in radiuses:
        positions[radius[1]] = (radius[2], radius[3])
    output = ""
    for position in positions:
        output += "%.1f %.1f " % (position[0], position[1])
    return output.strip()

def solve(N, W, L, radiuses):
    i = 0
    radius = radiuses[i]
    w1 = radius[0]
    l1 = L - radius[0]
    radius[2] = 0
    radius[3] = 0

    i += 1
    if i == N:
        return genResult(radiuses)
    radius = radiuses[i]
    if l1 > radius[0]:
        l1 -= radius[0]
        radius[2] = 0
        radius[3] = L
        ln = radius[0]
        
        i += 1
        if i == N:
            return genResult(radiuses)
        radius = radiuses[i]
        while l1 > 2 * radius[0]:
            l1 -= 2 * radius[0]
            radius[2] = 0
            radius[3] = L - (l1 + ln + radius[0])

            i += 1
            if i == N:
                return genResult(radiuses)
            radius = radiuses[i]
        
    w2 = W - radius[0]
    l2 = L - radius[0]
    radius[2] = W
    radius[3] = 0

    i += 1
    if i == N:
        return genResult(radiuses)
    radius = radiuses[i]
    if l2 > radius[0]:
        l2 -= radius[0]
        radius[2] = W
        radius[3] = L
        ln = radius[0]

        i += 1
        if i == N:
            return genResult(radiuses)
        radius = radiuses[i]
        while l2 > 2 * radius[0]:
            l2 -= 2 * radius[0]
            radius[2] = W
            radius[3] = L - (l2 + ln + radius[0])

            i += 1
            if i == N:
                return genResult(radiuses)
            radius = radiuses[i]

    while i < N:
        w1m = w1 + radius[0]
        w1 += 2 * radius[0]
        l1 = L - radius[0]
        radius[2] = w1m
        radius[3] = 0

        i += 1
        if i == N:
            return genResult(radiuses)
        radius = radiuses[i]
        if l1 > radius[0]:
            l1 -= radius[0]
            radius[2] = w1m
            radius[3] = L
            ln = radius[0]

            i += 1
            if i == N:
                return genResult(radiuses)
            radius = radiuses[i]
            while l1 > 2 * radius[0]:
                l1 -= 2 * radius[0]
                radius[2] = w1m
                radius[3] = L - (l1 + ln + radius[0])

                i += 1
                if i == N:
                    return genResult(radiuses)
                radius = radiuses[i]
    
    if w1 > s2:
        print "ERROR!"
    return genResult(radiuses)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit();

    inFile = open(sys.argv[1])
    outFile = open(sys.argv[2], "w")

    startTime = datetime.datetime.now()
    print "Start Time = %s" % startTime
    print SEPARATE_LINE

    T = int(inFile.readline())
    for i in range(T):
        N, W, L = map(int, inFile.readline().strip().split())
        radiuses = list()
        j = 0
        inLine = inFile.readline().strip().split()
        for radius in inLine:
            # last two are initial position
            radiuses.append([int(radius), j, -1, -1])
            j += 1
        if N != len(radiuses):
            print "ERROR! N=%d, radiuses=%s" % (N, radiuses)
        radiuses.sort(key = lambda radius : radius[0], reverse = True)
        print "radiuses=%s" % radiuses
        result = solve(N, W, L, radiuses)
        outFile.write("Case #%d: %s\n" % (i + 1, result))
    endTime = datetime.datetime.now()

    print SEPARATE_LINE
    print "End Time = %s" % endTime
    print "Cost Time = %s" % (endTime - startTime)
    inFile.close()
    outFile.close()
