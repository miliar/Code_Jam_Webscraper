#!/usr/bin/env python

import fileinput

for i, line in enumerate(fileinput.input()):
    if i == 0: continue

    stuff = line.rstrip().split(' ')
    c = int(stuff[0])
    combiners = stuff[1:c+1]
    stuff = stuff[c+1:]

    d = int(stuff[0])
    opposers = stuff[1:d+1]
    stuff = stuff[d+1:]

    str = stuff[1]

    #print combiners, opposers, str

    stack = []

    for c in str:
        if not stack:
            stack = [c]
            continue
        last = stack[-1]
        for com in combiners:
            if com[0] == c and com[1] == last or com[1] == c and com[0] == last:
                stack[-1] = com[2]
                break
        else:
            stack.append(c)
            for opp in opposers:
                if opp[0] in stack and opp[1] in stack:
                    stack = []
                    break
    print "Case #%d: [%s]" % (i, ', '.join(stack))

