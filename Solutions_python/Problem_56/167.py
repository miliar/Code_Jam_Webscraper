def solve(n,k,b):
    win = {'R':False,'B':False}
    sol = {}
    for r in range(-1,n):
        sol[r,-1] = [0,0,0,0]
        sol[-1,r] = [0,0,0,0]
        sol[r,n] = [0,0,0,0]
        sol[-1,n] = [0,0,0,0]
    for r in range(n):
        for c in range(n):
            b[r,c]
            sol[r,c] = [1+(sol[r,c-1][0] if b[r,c] == b[r,c-1] else 0),
                        1+(sol[r-1,c-1][1] if b[r,c] == b[r-1,c-1] else 0),
                        1+(sol[r-1,c][2] if b[r,c] == b[r-1,c] else 0),
                        1+(sol[r-1,c+1][3] if b[r,c] == b[r-1,c+1] else 0)
                        ]
            if max(sol[r,c]) >= k:
                win[b[r,c]] = True
    return ['Neither','Red','Blue','Both'][1*int(win['R']) + 2*int(win['B'])]

T = input()
for case in xrange(1,T+1):
    n,k = map(int,raw_input().split())
    b = {}
    for r in range(-1,n):
        b[r,-1] = [0,0,0,0]
        b[-1,r] = [0,0,0,0]
        b[r,n] = ''
        b[-1,n] = [0,0,0,0]
    for r in range(n):
        l = raw_input().replace('.','').rjust(n,'.')
        for c in range(n):
            b[r,c] = l[c]
    print "Case #%s: %s" % (case, solve(n,k,b))
