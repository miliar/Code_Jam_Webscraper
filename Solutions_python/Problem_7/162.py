#!/usr/bin/env python

FNAME = "A-small-attempt0.in"

class Case(object):
    def __init__(self, coords):
        self.coords = coords
            
def getcentroid(c1, c2, c3):
    xsum = c1[0] + c2[0] + c3[0]
    ysum = c1[1] + c2[1] + c3[1]
    return xsum % 3 == 0 and ysum % 3 == 0

def combinations(items, n):
    if n==0: yield []
    else:
        for i in xrange(len(items)):
            for cc in combinations(items[i+1:],n-1):
                yield [items[i]]+cc 


def getnumtrigs(coords):
    s = 0
    combos = combinations(coords, 3)
    for combo in combos:
        c = getcentroid(*combo)
        if c:
            s += 1
    return s

def getcoords(n, A, B, C, D, x0, y0, M):
    coords = []
    X = x0
    Y = y0
    coords.append((X, Y))
    for i in range(n - 1):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        coords.append((X, Y))
    return coords

def parse(lines):
    cases = []
    for line in lines[1:]:
        ints = [int(value) for value in line.split()]
        cases.append(Case(getcoords(*ints)))     
    return cases
        
if __name__ == "__main__":
    lines = file(FNAME).read().splitlines()
    cases = parse(lines)
    answers = [getnumtrigs(case.coords) for case in cases]
    outlines = ["Case #%d: %d\n" % (i + 1, answer) for i, answer in enumerate(answers)]
    file(FNAME + ".out", "w").writelines(outlines)

