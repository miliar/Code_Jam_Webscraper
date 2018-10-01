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

def solve(picture):

    for i in xrange(len(picture)):
        try:
            for j in xrange(len(picture[i])):
                if picture[i][j] == '#' and picture[i][j+1] == '#' and \
                        picture[i+1][j] == '#' and picture[i+1][j+1] == '#':
                            picture[i][j] = '/'
                            picture[i][j+1] = '\\'
                            picture[i+1][j] = '\\'
                            picture[i+1][j+1] = '/'
        except IndexError:
            print("Impossible")
            return

    for i in picture:
        if '#' in i:
            print("Impossible")
            return

    for i in picture:
        for j in i:
            sys.stdout.write(j)
        sys.stdout.write('\n')

if __name__ == '__main__':
    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        picture = []
        rows, cols = map(int, sys.stdin.readline().split())

        for j in xrange(rows):
            line = sys.stdin.readline()[:-1]
            row = []

            for k in xrange(len(line)):
                row.append(line[k])

            picture.append(row)

        print("Case #%d:" % (i+1,))
        solve(picture)

# vim: ai ts=4 sts=4 et sw=4
