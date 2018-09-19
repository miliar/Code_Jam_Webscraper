from __future__ import with_statement
import sys

def neighbors(m, i, j):
    return [m[i-1 if i>0 else i][j],
            m[i][j-1 if j>0 else j],
            m[i][j+1 if j<W-1 else j],
            m[i+1 if i<H-1 else i][j]]

def follow(t):
    i, j = t
    if isinstance(results[i][j], int):
        return results[i][j]
    else:
        return follow(results[i][j])

def seen(item):
    global sink
    if item not in have_seen:
        have_seen[item] = sink
        sink = chr(ord(sink)+1)
    return have_seen[item]

vec = {0: (-1, 0), 1: (0, -1), 2: (0, 1), 3: (1, 0)}

with open(sys.argv[1]) as f:
    num_maps = int(f.readline())

    for m in xrange(num_maps):
        H, W = map(int, f.readline().split())
        have_seen = {}
        sink = 'a'
        
        this_map = [map(int, f.readline().split()) for r in xrange(H)]
        results = [[0 for j in xrange(W)] for i in xrange(H)]
        my_sink = 1
        for i, row in enumerate(this_map):
            for j, col in enumerate(row):
                me = this_map[i][j]
                n = neighbors(this_map, i, j)
                if all((me <= x for x in n)):
                    results[i][j] = my_sink
                    my_sink += 1
                else:
                    y, x = vec[n.index(min(n))]
                    results[i][j] = (i+y, j+x)

        print "Case #%d:" % (m+1)
        for i, row in enumerate(results):
            print ' '.join((seen(k) for k in
                            (follow((i,j)) for j, col in enumerate(row))))
