#!/usr/bin/env python
#
#  Problems of Programming Contests
#  ================================
#
#  Jose Ignacio Galarza (igalarzab)
#  <igalarzab@gmail.com>
#  http://sysvar.net
#

import sys

def solve(n, pd, pg):
    if pg == 100 and pd != 100:
        return "Broken"

    if pg == 0 and pd != 0:
        return "Broken"

    if pg == 0:
        return "Possible"

    for i in xrange(1, n+1):
        if 100 % i != 0:
            continue

        it = 100 / i
        for j in xrange(it, 101, it):
            if j == pd:
                return "Possible"

    return "Broken"

if __name__ == '__main__':
    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        nums = map(int, sys.stdin.readline().split())
        print("Case #%d: %s" % (i+1, solve(nums[0], nums[1], nums[2])))

# vim: ai ts=4 sts=4 et sw=4
