#!/usr/bin/python

import sys

def solve(case):
    orange = 1
    orange_t = 0
    blue = 1
    blue_t = 0
    seconds = 0

    for step in case:
        if step[0] == 'O':
            # Time taken to move from current position to next
            to_move = abs(step[1] - orange)
            # Substract free time
            to_move -= seconds - orange_t
            to_move = max(0, to_move)
            # Move to position
            orange = step[1]
            # Move and press
            seconds += to_move + 1
            orange_t = seconds
        elif step[0] == 'B':
            to_move = abs(step[1] - blue)
            to_move -= seconds - blue_t
            to_move = max(0, to_move)
            blue = step[1]
            seconds += to_move + 1
            blue_t = seconds

    return seconds

def main(data = "A-example.in"):
    f = open(data, 'r')
    inp = map(lambda x: x[:-1], f.readlines())

    T = int(inp[0])
    cases = []
    for l in inp[1:]:
        case = []
        ll = l.split(' ')
        steps = int(ll[0])
        j = 0
        i = 1
        while j < steps:
            case.append((ll[i], ll[i+1]))
            i += 2
            j += 1
        cases.append(map(lambda x: (x[0], int(x[1])), case))

    i = 1
    for case in cases:
        print "Case #" + str(i) + ": " + str(solve(case))
        i += 1

if len(sys.argv) == 2:
    main(sys.argv[1])
else:
    print sys.argv[0] + " <input file>"
