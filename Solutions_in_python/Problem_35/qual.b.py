#!/usr/bin/python

from common import *

alpha = 'abcdefghijklmnopqrstuvwxyz'

h = -1
w = -1
altitudes = None
basins = None

infinity = 10000000

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

cur_sink_index = 0

def alt(row, col):
    if row < 0 or row >= h or col < 0 or col >= w:
        return infinity
    return altitudes[row][col]

def find_sink(row, col):
    global cur_sink_index

    if basins[row][col]:
        return basins[row][col]

    me = alt(row, col)

    lowest = me
    for i in xrange(len(dx)):
        temp = alt(row + dy[i], col + dx[i])
        if temp < lowest:
            lowest = temp

    if lowest == me:
        # we are a sink
        basins[row][col] = alpha[cur_sink_index]
        cur_sink_index += 1
        return basins[row][col]

    for i in xrange(len(dx)):
        if lowest == alt(row + dy[i], col + dx[i]):
            b = find_sink(row + dy[i], col + dx[i])
            basins[row][col] = b
            return b

def testcase(x):
    global h, w, altitudes, basins, cur_sink_index
    h, w = readintegers()

    altitudes = []
    for row_index in xrange(h):
        altitudes.append(readintegers())

    basins = []
    for row in xrange(h):
        basins.append([''] * w)

    cur_sink_index = 0
    for row in xrange(h):
        for col in xrange(w):
            find_sink(row, col)

    writeline("Case #%d:" % x)
    for row in xrange(h):
        out_line = []
        for col in xrange(w):
            out_line.append(basins[row][col])
        writeline(' '.join(out_line))

run_tests(sys.argv, testcase)
