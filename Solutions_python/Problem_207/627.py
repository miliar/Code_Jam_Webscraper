#!/usr/bin/env python

import math

def place(num, c, stalls):
    if stalls.count(0) == len(stalls):
        if 3 * num == len(stalls):
            num_double_spaced = num
        else:
            num_double_spaced = len(stalls) % num
        prev = None
        spacing = 0
        for i in xrange(len(stalls)):
            if i == 0:
                stalls[i] = c
                spacing = 0
            elif spacing == 0:
                spacing += 1
            elif spacing == 1:
                if num_double_spaced > 0:
                    spacing += 1
                    num_double_spaced -= 1
                else:
                    stalls[i] = c
                    spacing = 0
            else:
                stalls[i] = c
                spacing = 0
    else:
        num_placed = 0
        prev = None
        for i in xrange(len(stalls)):
            if stalls[i] == 0 and prev is not c and num_placed != num:
                stalls[i] = c
                num_placed += 1
            prev = stalls[i]
    if stalls.count(c) != num:
        print "**********ERROR*************", num, c, stalls.count(c)

t = int(raw_input())
for i in xrange(1, t + 1):
    n, r, o, y, g, b, v = [int(s) for s in raw_input().split(" ")]
    stalls = [0] * n
    max_num = math.floor(n/2.0)
    reds = (r,o,v)
    yellows = (o,y,g)
    blues = (g,b,v)
    if sum(reds) > max_num or sum(yellows) > max_num or sum(blues) > max_num:
        print "Case #{}: {}".format(i, "IMPOSSIBLE")
        continue
    
    if sum(reds) >= sum(yellows) and sum(reds) >= sum(blues):
        place(r, 'R', stalls)
        if sum(yellows) >= sum(blues):
            place(y, 'Y', stalls)
            place(b, 'B', stalls)
        else:
            place(b, 'B', stalls)
            place(y, 'Y', stalls)
    elif sum(yellows) >= sum(blues):
        place(y, 'Y', stalls)
        if sum(reds) >= sum(blues):
            place(r, 'R', stalls)
            place(b, 'B', stalls)
        else:
            place(b, 'B', stalls)
            place(r, 'R', stalls)
    else:
        place(b, 'B', stalls)
        if sum(reds) >= sum(yellows):
            place(r, 'R', stalls)
            place(y, 'Y', stalls)
        else:
            place(y, 'Y', stalls)
            place(r, 'R', stalls)

    print "Case #{}: {}".format(i, ''.join(stalls))
