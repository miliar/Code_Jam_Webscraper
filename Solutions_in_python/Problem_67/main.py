#!/usr/bin/env python
import fileinput

def main():
    reader = fileinput.input()
    trials = int(reader.next())
    for t in range(1, trials+1):
        result = trial(reader)
        print "Case #%d: %s" % (t, result)

def ints(reader):
    return [int(k) for k in reader.next().strip().split()]

def trial(reader):
    nr = int(reader.next())
    if nr == 0: return 0
    rects = []
    for k in range(nr):
        rects.append(ints(reader))
    xlen, ylen = 0, 0
    for x1, y1, x2, y2 in rects:
        xlen = max(x2 + 1, xlen)
        ylen = max(y2 + 1, ylen)
    a = makeArray(xlen, ylen)
    for x1, y1, x2, y2 in rects:
        fill(a, x1, y1, x2, y2)
    n = 0
    #report(a)
    while True:
        a, live = evolve(a)
        #report(a)
        n += 1
        if not live: break
    return n

def report(a):
    print '--'
    for x in range(len(a)):
        print a[x]

def fill(a, x1, y1, x2, y2):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            a[x][y] = 1

def makeArray(nx, ny):
    a = [0] * nx
    for x in range(nx):
        a[x] = [0] * ny
    return a

def evolve(a):
    xlen, ylen = len(a), len(a[0])
    b = makeArray(xlen, ylen)
    live = False
    for x in range(xlen):
        for y in range(ylen):
            if a[x][y]:
                if ((0 < x and a[x-1][y]) or
                    (0 < y and a[x][y-1])):
                    b[x][y] = 1
                    live = True
            else:
                if ((0 < x and a[x-1][y]) and
                    (0 < y and a[x][y-1])):
                    b[x][y] = 1
                    live = True
    return b, live


main()
