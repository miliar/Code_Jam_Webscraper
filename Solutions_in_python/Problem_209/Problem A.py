#!/usr/bin/env python

import sys
from operator import itemgetter
import math

def getSideSurface(r, h):
    return 2 * math.pi * r * h

def getCircleArea(r):
    return r ** 2 * math.pi

def getCircularSection(r1, r2):
    return getCircleArea(r2) - getCircleArea(r1)

def solve(N, K, P):
    P_s = sorted(P, key=itemgetter(0), reverse=True)
    print(P_s, file =sys.stderr)

    area = 0
    R_prev = -1
    H_prev = 0
    for R, H in P_s:
        if R != R_prev:
            area += getSideSurface(R_prev, H_prev)
            area += getCircularSection(R_prev, R)
            R_prev = R
            H_prev = 0
        else:
            H_prev += H
    
    area += getSideSurface(R_prev, H_prev)
    area += getCircularSection(0, R_prev)

    return area

def solve2(N, K, P):

    areas = []
    for R, H in P:
        areas.append((getSideSurface(R, H), R))
    
    ordered_areas = sorted(areas, key=itemgetter(0), reverse=True)
    print(ordered_areas, file =sys.stderr)

    ris = ordered_areas[:K]

    area1 = getCircleArea(max([R for A, R in ris]))

    for A, R in ordered_areas[K:]:
        if area1 < getCircleArea(R) - ris[-1][0] + A:
            ris[-1] = (A, R)
            area1 = getCircleArea(max([Ra for A, Ra in ris]))

    area = getCircleArea(max([R for A, R in ris]))
    area += sum([A for A, R in ris])
    
    return area

def main():
    case_counter = 1

    T = int(input())  # read a line with a single integer

    for i in range(1, T + 1):

        print("Processing Case #{}".format(case_counter), file =sys.stderr)
        
        # INPUT
        N, K = [int(s) for s in input().split(" ")]

        P = [tuple(input().split(" ")) for x in range(N)]
        P = [(int(x[0]),int(x[1])) for x in P]
        print(P, file =sys.stderr)

        # SOLVE
        solution = solve2(N, K, P)

        # OUTPUT
        print("Case #{0}: {1:.9f}".format(case_counter, solution))

        case_counter += 1


if  __name__ =='__main__':
    main()
