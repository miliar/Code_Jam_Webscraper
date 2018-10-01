import math
import re

fp = open('A-small-attempt0.in')

cases = int(fp.readline())
case = 0

for case in range(0, cases):
    line = map(int, fp.readline().split(" "))
    n = line[0]
    A = line[1]
    B = line[2]
    C = line[3]
    D = line[4]
    x0 = line[5]
    y0 = line[6]
    M = line[7]
    
    pts = []
    pts.append((x0, y0))
    X = x0
    Y = y0
    for i in range(1, n):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        pts.append((X,Y))
    
    lp = len(pts)
    tri = 0
    for i in range(0, lp):
        for j in range(i + 1, lp):
            for k in range(j + 1, lp):
                cx = (pts[i][0] + pts[j][0] + pts[k][0]) / 3.0
                cy = (pts[i][1] + pts[j][1] + pts[k][1]) / 3.0
                if cx == int(cx) and cy == int(cy):
                    tri += 1

    print "Case #%i: %i" % (case + 1, tri)

fp.close()
