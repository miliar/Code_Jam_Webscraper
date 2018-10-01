#!/usr/bin/env python3
import math

def intLine():
    return list(map(int, input().split()))


cases = intLine()[0]
case = 0
while case < cases:
    case += 1

    radius, availablePaint = intLine()
    circles = 0
    paintUsed = 0
    while True:
        paintUsed += (radius+1)**2 - radius**2
        if paintUsed > availablePaint:
            break
        circles += 1
        radius += 2

    print('Case #{0}: {1}'.format(case, circles))
