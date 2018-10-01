#
# Google Code Jam 2010
# (C) Andrew Tutt
#
# Code Jam Skeleton
#

from time import sleep, clock
import os

from copy import copy

IN_FILENAME = 'input.txt'
OUT_FILENAME = 'output.txt'

def solver(c):

    count = 0

    cdel = copy(c)

    for i in c:
        tmp = cdel[0]
        del cdel[0]
        for i in cdel:
            if int(tmp[0]) < int(i[0]) and int(tmp[1]) > int(i[1]):
                count += 1
            if int(tmp[0]) > int(i[0]) and int(tmp[1]) < int(i[1]):
                count += 1

    print(count)
    return count

if __name__ == '__main__':
    clock()
    f = open(IN_FILENAME, 'r')
    total_cases = int(f.readline())

    t_range = range(1,total_cases+1)
    olist = list(range(1,total_cases+2))

    # Read in the problems
    for case_number in t_range:
        coords = []
        numwires = int(f.readline())
        for wires in range(numwires):
            coords.append(tuple(f.readline().strip().split(' ')))
        
        olist[case_number] = solver(coords)

    f = open(OUT_FILENAME, 'w')
    for c in t_range:
        f.write("Case #" + str(c) + ": " + str(olist[c])+"\n")

    print(str(clock()) + " seconds")

