import os, sys, string

f = file('B-large.in', 'r')

dir = ((-1, 0), (0, -1), (0, 1), (1, 0))

def test_case(ncase):
    (h, w) = map(int, f.readline().split())
    m = []
    for i in range(h):
        m.append(map(int, f.readline().split()))
    
    flow_to = [[-1] * w for i in range(h)]
    for r in range(h):
        for c in range(w):
            me = m[r][c]
            for d in range(4):
                nr, nc = r+dir[d][0], c+dir[d][1]
                if nr >= 0 and nc >= 0 and nr < h and nc < w and m[nr][nc] < me:
                    me = m[nr][nc]
                    flow_to[r][c] = d
    
    regn = [[-1] * w for i in range(h)]
    global nextregn
    nextregn = 0
    def fillrgn(r, c):
        global nextregn
        if regn[r][c] != -1:
            return regn[r][c]
        if flow_to[r][c] == -1:
            regn[r][c] = nextregn
            nextregn += 1
            return regn[r][c]
        else:
            t = flow_to[r][c]
            regn[r][c] = fillrgn(r+dir[t][0], c+dir[t][1])
            return regn[r][c]
    for r in range(h):
        for c in range(w):
            if regn[r][c] == -1:
                fillrgn(r, c)
    print 'Case #%d:' % ncase
    for r in range(h):
        print ' '.join([string.lowercase[i] for i in regn[r]])

T = int(f.readline())
for i in range(1, T+1):
    test_case(i)
    #break
