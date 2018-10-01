def solve(test):    
    n, q = map(int, raw_input().split())

    ttl = [0] * n
    s = [0] * n

    u = [0] * q
    v = [0] * q

    r = []

    for i in xrange(n):
        ttl[i], s[i] = map(int, raw_input().split())

    for i in xrange(n):
        r.append (map(int, raw_input().split()))

    for i in xrange(q):
        u[i], v[i] = map(int, raw_input().split())
        u[i] -= 1
        v[i] -= 1

    
    t = [ [0]*n for i in xrange(n) ]

    for h in xrange(n):
        best = [-1] * n
        best[h] = 0
        l = [(h, ttl[h])]        
        while len(l) > 0:
            l2 = []
            for cc in l:
                c1 = cc[0]
                tl = cc[1]
                for c2 in xrange(n):
                    if r[c1][c2] != -1 and r[c1][c2]<=tl:
                        if best[c2] == -1 or best[c2]> best[c1] + float(r[c1][c2])/s[h]:
                            best[c2] = best[c1] + float(r[c1][c2])/s[h]
                            l2.append((c2, tl-r[c1][c2]))
            l = l2
        t[h] = best
    
    l = [0]
    best = [-1] * n
    best[0] = 0

    while len(l) > 0:
        l2 = []
        for c1 in l:
            for c2 in xrange(n):
                if t[c1][c2] != -1:
                    if best[c2] == -1 or best[c1] + t[c1][c2] < best[c2]:
                        best[c2] = best[c1] + t[c1][c2]
                        l2.append(c2)
        l = l2

    print best[-1]

    #print result


def create_array(*sizes):
   return [0 if len(sizes)==1 else create_array(*sizes[1:]) for x in xrange(sizes[0])]




import sys
sys.stdin = open(sys.argv[1] if len(sys.argv) > 1 else "sample.in")

for test in range(input()):
    print "Case #{}:".format(test+1),
    answer = solve(test)
    if answer != None:
        print answer


