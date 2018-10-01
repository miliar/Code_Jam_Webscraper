#!env python2

import sys


def is_possible_to_mow(lines):
    width = len(lines[0])
    height = len(lines)

    heights = []
    widths = []

    for line in lines:
        heights.append(max(line))

    for x in range(width):
        widths.append(max([l[x] for l in lines]))

    for x in range(width):
        for y in range(height):
            expected_height = min(widths[x], heights[y])
            if lines[y][x] != expected_height:
                return False

    return True


def read_input():
    count = int(sys.stdin.readline().strip())

    for _ in range(count):
        height, width = map(int, sys.stdin.readline().strip().split(' '))
        lines = []

        for _ in range(height):
            line = map(int, sys.stdin.readline().strip().split(' '))
            lines.append(line)

        yield lines


case = 1
for lines in read_input():
    possible = is_possible_to_mow(lines)
    result = "YES" if possible else "NO"
    print "Case #%d: %s" % (case, result)
    case += 1
