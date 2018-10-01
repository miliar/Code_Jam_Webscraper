import string
import sys

T = int(sys.stdin.readline())

def nbrs(m, h, w):
    global H
    global W
    inds = ((h+dh, w+dw) for (dh, dw) in [(-1, 0), (0, -1), (0, 1), (1, 0)])
    return ((m[hi][wi], hi, wi)
            for hi, wi in inds if 0 <= hi < H and 0 <= wi < W)

def flowto(m, h, w):
    best = (m[h][w], -1, -1)
    for n in nbrs(m, h, w):
        if n[0] < best[0]:
            best = n
    return best

for t in xrange(T):
    H, W = map(int, sys.stdin.readline().split(" ")[:2])
    m = [None] * H
    for h in xrange(H):
        m[h] = map(int, sys.stdin.readline().split(" ")[:W])
    print "Case #%d:" % (t+1)
    a = [[" " for w in xrange(W)] for h in xrange(H)]
    cli = 0
    def solve(m, a, h, w):
        global cli
        if a[h][w] != " ":
            return a[h][w]
        _, hl, wl = flowto(m, h, w)
        if hl == -1:  # sink
            a[h][w] = string.letters[cli]
            cli += 1
            return a[h][w]
        ans = solve(m, a, hl, wl)
        a[h][w] = ans
        return a[h][w]
    for h in xrange(H):
        for w in xrange(W):
            solve(m, a, h, w)
    for h in xrange(H):
        print " ".join(a[h])
