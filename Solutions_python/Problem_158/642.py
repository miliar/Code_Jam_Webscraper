from __future__ import print_function

import sys

fin = sys.stdin

num_cases = int(fin.readline().strip())

for C in range(num_cases):
    def p(name):
        # print("Case #{}: {} ({},{},{})".format(C+1, name, x, r, c))
        print("Case #{}: {}".format(C+1, name))

    x, r, c = [int(a) for a in fin.readline().split()]
    if x >= 7:
        p("RICHARD")
        continue

    if ((r*c) % x) != 0:
        p("RICHARD")
        continue

    if x > r and x > c:
        p("RICHARD")
        continue

    t1 = x // 2 + 1
    t2 = x - t1 + 1

    assert t1 + t2 -1 == x

    if (t1 > r or t2 > c) and (t1 > c or t2 > r):
        p("RICHARD")
        continue

    mit = min(t1,t2)
    mat = max(t1,t2)

    mis = min(r,c)
    mas = max(r,c)

    if mit > 1 and mat > mit and mit == mis:
        p("RICHARD")
        continue



    p("GABRIEL")