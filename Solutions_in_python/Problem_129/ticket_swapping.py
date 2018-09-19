import bisect
N = 10**10

def C(d):
    return d * (d-1) // 2

#B = C(5) + C(5)
#print C(4) + C(6) - B
#print C(3) + C(7) - B
#print C(2) + C(8) - B

def solve(prob):
    base = 0
    for o, e, p in prob:
        base += C(e-o) * p

    S = 0
    while S < len(prob):
        prob.sort()

        o, e, p = prob[S]
        t = bisect.bisect_right(prob, [e, N+1])
        #print S, e, t

        X = prob[S+1:t]
        X.sort(key=lambda L: (-L[1], -L[0]))
        #print prob
        #print X

        for i in range(len(X)):
            oo, ee, pp = X[i]
            #print o, e, p, '<=>', oo, ee, pp
            if ee <= e:
                S += 1
                break
            if oo <= o:
                continue
            if p == pp:  # just swap
                #print "p == pp", p, pp
                prob[S][1] = ee
                X[i][1] = e
                break
            elif p < pp: # All p swaps.
                #print "p < pp", p, pp
                prob[S][1] = ee
                X[i][2] = pp - p
                prob.append([oo, e, p])
                break
            # p > pp, All pp swaps
            #print "p > pp", p, pp
            X[i][1] = e
            prob.append([o, ee, pp])
            p -= pp
            prob[S][2] = p
        else:
            S += 1

    after = 0
    for o, e, p in prob:
        after += C(e-o) * p

    return after - base


import sys
T = int(sys.stdin.readline())
for i in range(1, T+1):
    N, M = map(int , sys.stdin.readline().split())
    prob = []
    for _ in range(M):
        prob.append(map(int, sys.stdin.readline().split()))
    X = solve(prob)

    print "Case #%d: %d" % (i, X)
