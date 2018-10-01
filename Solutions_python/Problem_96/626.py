#!/usr/bin/python

import re
from sys import stdin


def best_nonsurprising_triplet(total_points):
    triplet = [total_points / 3] * 3
    for i in range(total_points % 3):
        triplet[i] += 1
    return triplet

def dancers(points, surprising, minp):
    total = 0
    points = sorted(points, lambda x,y: cmp(y, x))
    
    for total_points in points:
        triplet = best_nonsurprising_triplet(total_points)
        if triplet[0] >= minp:
            total += 1
        elif triplet[0] + 1 == minp:
            if surprising == 0: break
            if triplet[0] == triplet[1] and triplet[0] > 0:
                surprising -= 1
                total += 1
        if triplet[0] + 1 < minp and surprising == 0: break
    return total


ncases = int(stdin.readline().strip())

for i, line in enumerate(stdin.xreadlines()):
    line = re.split(' +', line.strip())
    n, s, p, points = int(line[0]), int(line[1]), int(line[2]), [int(j) for j in line[3:]]
    print("Case #%i: %i" % (i+1, dancers(points, s, p)))
