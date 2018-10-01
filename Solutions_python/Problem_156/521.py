#!/usr/bin/python3

import sys
import math

ncases = int(sys.stdin.readline().strip())

for t in range(1, ncases+1):
    d = int(sys.stdin.readline().strip())
    values = sys.stdin.readline().strip().split()
    pancakes = [int(x) for x in values]

    pancakes.sort(reverse=True)
    best = pancakes[0]

    # Node format: List of diners with pancakes, number of special minutes
    initial_node = [pancakes, 0]
    queue = [initial_node]

    while queue:
        node = queue.pop(0)
        diners = node[0]
        special = node[1]

        top = diners[0]

        #if (top + special) >= best:
        #    continue

        if (top + special) < best:
            best = top + special

        if top < 4:
            continue

        # Let's introduce new special minutes. Note _all_ diners with
        # the max number of pancakes should be split (adding more special
        # minuts), as splitting just one of them is stupid
        for n in [2, 3, 4]:
            splits = []
            remainder = top
            for i in range(0, n):
                split = math.floor(remainder/(n-i))
                remainder -= split
                splits.append(split)

            diners_after_special = list(diners)
            new_special = special
            while diners_after_special[0] == top:
                diners_after_special.pop(0)
                diners_after_special += splits
                new_special += (n-1)

            diners_after_special.sort(reverse=True)
            new_node = [diners_after_special, new_special]
            queue.append(new_node)
    

    print("Case #{0}: {1}".format(t, best))

