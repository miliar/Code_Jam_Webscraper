def check(M, letter, r1, r2, c1, c2):
    #print 'check', M, letter, r1, r2, c1, c2
    return all(M[rr][cc] == '?' for rr in xrange(r1, r2+1) for cc in xrange(c1, c2+1) if M[rr][cc] != letter)

def f():
    tc, = map(int, raw_input().split())
    for _tc in xrange(tc):
        R, C = map(int, raw_input().split())
        M = []
        for r in xrange(R):
            M.append(list(raw_input().strip()))
        ini = set()
        for r in xrange(R):
            for c in xrange(C):
                if M[r][c] != '?': 
                    ini.add((r,c))
        for r, c in ini:
            r1, c1 = r2, c2 = r, c
            letter = M[r][c]
            expand = True
            while expand:
                if c2+1 < C and check(M, letter, r1, r2, c1, c2+1):
                    c2 = c2+1
                elif c1 > 0 and check(M, letter, r1, r2, c1-1, c2):
                    c1 = c1 -1 
                elif r1 > 0 and check(M, letter, r1-1, r2, c1, c2):
                    r1 = r1 -1 
                elif r2+1 < R and check(M, letter, r1, r2+1, c1, c2):
                    r2 = r2 + 1
                else:
                    expand = False
            for rr in xrange(r1, r2+1):
                for cc in xrange(c1, c2+1):
                    M[rr][cc] = letter
        print 'Case #%d:' % (_tc+1,)
        for rr in xrange(R): print ''.join(M[rr])
f()


