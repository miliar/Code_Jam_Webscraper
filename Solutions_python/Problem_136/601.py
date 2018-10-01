#!/usr/local/bin/python

from sys import stdin

lines = stdin.read().splitlines()
num_cases = int(lines[0])
for case in xrange(num_cases):
    row = lines[case + 1].split()
    row = map(float, row)
    cost = row[0]
    rate = row[1]
    total = row[2]
    time = 0
    count = 0
    while (total / (2 + ((count + 1) * rate)) + (cost / (2 + (count * rate))) < total / (2 + (count * rate))):
        time += cost / (2 + (count * rate))
        count += 1
    time += total / (2 + (count * rate))
    print "Case #{0}: {1}".format(case + 1, time)
