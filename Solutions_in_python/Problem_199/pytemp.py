#!/opt/local/bin/python

import sys
import re

T = int(sys.stdin.readline())
for casenum in range(T):
    data = sys.stdin.readline().split()
    cakes = data[0]
    flipper = int(data[1])
    flips = 0
    parity = [0 if x == '+' else 1 for x in cakes]
    for i in range(0, len(cakes) - flipper + 1):
        if parity[i] % 2:
            flips += 1
            for j in range(i, i+flipper):
                parity[j] += 1
    success = flips
    for i in range(len(cakes) - flipper + 1, len(cakes)):
        if parity[i] % 2:
            success = "IMPOSSIBLE"
    print("Case #" + str(casenum + 1) + ": " + str(success))
