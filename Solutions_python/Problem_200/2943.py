#! /usr/bin/env python

import sys

firstnumbers = []


def istidy(n):
    return ''.join(sorted(n)) == ''.join(n)


def lasttidy(n):
    result = ''
    for digit in reversed(n):
        result = digit + result
        if istidy(result):
            continue

        nontidy = int(''.join(result[:2]))
        result = str(firstnumbers[nontidy]) + '9' * len(result[2:])
    assert(int(n) >= int(result))
    return int(result)


if __name__ == '__main__':
    last = None
    for i in range(0, 100):
        current = str(i)
        if istidy(current):
            firstnumbers.append('%02d' % int(current))
            last = current
        else:
            firstnumbers.append('%02d' % int(last))
        #print(i, firstnumbers[i])

    with open(sys.argv[1]) as f:
        lines = f.readlines()
    for index, line in enumerate(lines[1:]):
        sys.stdout.write("Case #%s: " % (index + 1))
        N = line.strip()
        print(lasttidy(N))
