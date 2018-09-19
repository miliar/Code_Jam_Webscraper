#!/usr/bin/env python
import sys

lawn = []

filename = sys.argv[1]
f = open(filename)
num_cases = int(f.readline().strip())
for case in xrange(num_cases):
    N, M = [int(x) for x in f.readline().strip().split(" ")]
    lawn = []
    for i in xrange(N):
        lawn.append([100] * M)

    target_lawn = []
    heights = set([])
    cuttable = True
    for i in xrange(N):
        line = [int(x) for x in f.readline().strip().split(" ")]
        for n in line:
            heights.add(n)
        target_lawn.append(line)

    heights = list(heights)
    heights.sort()
    heights.reverse()
    for height in heights:
        for y in range(N):
            if height in target_lawn[y] and max(target_lawn[y]) == height:
                lawn[y] = [height] * M

        for x in range(M):
            column = [target_lawn[y][x] for y in xrange(N)]
            if height in column and max(column) == height:
                for y in xrange(N):
                    lawn[y][x] = height

    if lawn != target_lawn:
        print "Case #%d: NO" % (case + 1)
    else:
        print "Case #%d: YES" % (case + 1)

