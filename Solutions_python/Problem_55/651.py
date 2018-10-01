#!/usr/bin/env python
"""
Solution for Problem C of Qualification Round.

"""

import sys

def rollerCoaster(R, k, N, g):
    euros = 0
    start = 0
    queue = g[:]
    for r in xrange(R):
        groupsIn = []
        peopleIn = 0
        # Board people
        while len(queue) > 0:
            if peopleIn + queue[0] <= k:
                # We have enough space for the next group
                groupsIn.append(queue[0])
                peopleIn = sum(groupsIn)
                del queue[0]
            else:
                #We are full. Stop trying to board more people.
                break

        # Collect the money. 1 euro per person
        euros += peopleIn

        # Requeue the people
        queue.extend(groupsIn)

    return euros


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: %s [inputFile]"%sys.argv[0]
        exit(1)

    inputFileName = sys.argv[1]
    if inputFileName[-3:] == ".in":
        outputFileName = inputFileName[:-3]
    else:
        outputFileName = inputFileName
    outputFileName = outputFileName + ".out"

    inputFile  = open(inputFileName , "r")
    outputFile = open(outputFileName, "w")

    cases = inputFile.readline()
    cases = int(cases.strip())

    for case in xrange(cases):
        line1 = inputFile.readline().strip()
        line2 = inputFile.readline().strip()

        (R, k, N) = [int(x) for x in line1.split(" ")]
        g = [int(x) for x in line2.split(" ")]

        result = rollerCoaster(R, k, N, g)

        outputFile.write("Case #%d: %d\n"%(case+1, result))
