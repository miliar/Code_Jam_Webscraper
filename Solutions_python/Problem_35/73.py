#!/usr/bin/env python

import sys

basin_bottom = None

def bottom(a):
    while a in basin_bottom:
        b = basin_bottom[a]
        assert b < a
        a = b
    return a

def merge(a, b):
    ab = bottom(a)
    bb = bottom(b)
    m = min(ab,bb)
    if m != a: basin_bottom[a] = m
    if m != b: basin_bottom[b] = m
    if m != ab: basin_bottom[ab] = m
    if m != bb: basin_bottom[bb] = m
    
def find_basins(elevations):
    global basin_bottom
    basin_bottom = {}
    for r, row in enumerate(elevations):
	for c, height in enumerate(row):
            d = None
	    if r > 0 and elevations[r-1][c] < height:  # North
                d, height = (r-1,c), elevations[r-1][c]
	    if c > 0 and row[c-1] < height: # West
                d, height = (r,c-1), row[c-1]
	    if c+1 < len(row) and row[c+1] < height: # East
                d, height = (r,c+1), row[c+1]
	    if r+1 < len(elevations) and elevations[r+1][c] < height: # South
                d, height = (r+1,c), elevations[r+1][c]
            if d is not None:
                merge( (r,c), d )

    basins = {}
    letters = "abcdefghijklmnopqrstuvwxyz"

    out = []
    for r, row in enumerate(elevations):
        line = []
        for c, col in enumerate(row):
            b = bottom( (r,c) )
            if b not in basins:
                assert b == (r,c)
                basins[b] = letters[0]
                letters = letters[1:]
            line.append(basins[b])
        out.append(" ".join(line))
    return "\n".join(out) 


f = sys.stdin
tests = int(f.readline().strip())
for case in xrange(tests):
    h, w = map(int, f.readline().strip().split())

    elevations = []
    for row in xrange(h):
        elevations.append( map(int, f.readline().strip().split()) )
        assert len(elevations[-1]) == w

    print "Case #%d:" % (case+1)
    print find_basins(elevations)

