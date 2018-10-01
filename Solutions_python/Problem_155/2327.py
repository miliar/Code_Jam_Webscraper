#!/usr/bin/env python

import sys

LINES_PER_CASE = 1

def main():
    if len(sys.argv) > 1:
        input = sys.argv[1]
    else:
        input = "input.txt"

    try:
        with open(input) as f:
            content = f.readlines()
    except:
        print("Can not find input file: %s" % input)
        sys.exit()

    T = int(content[0])

    case = line = 1
    while case <= T:
        result = run_case(content[line])

        print("Case #%d: %s" % (case, result))
        line += LINES_PER_CASE
        case += 1


def run_case(case):
    c = case.split()

    peepsNeeded = 0

    maxShy = int(c[0])
    shyVals = c[1][::-1]

    return max([(maxShy - i) - (sum([int(x) for x in shyVals[(i+1):]])) for i in range(0, len(shyVals))])

main()
