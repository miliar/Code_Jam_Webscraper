from __future__ import division

def swap(A, i, j):
    tmp  = A[i]
    A[i] = A[j]
    A[j] = tmp

def can_make_it(x, v, B, T):
    return (B-x)/v <= T

def solve(X, V, K, B, T):
    X = list(reversed(X))
    V = list(reversed(V))
    found = 0
    swaps = 0
    for i in range(len(X)):
        if can_make_it(X[i], V[i], B, T):
            #print X[i], V[i], B, T
            found += 1
            if found == K:
                return swaps
            continue
        for j in range(i, len(X)+1):
            if j == len(X):
                return "IMPOSSIBLE"
            if can_make_it(X[j], V[j], B, T):
                break
        for k in range(j, i, -1):
            swap(X, k, k-1)
            swap(V, k, k-1)
            swaps += 1
        found += 1
        if found == K:
            return swaps
    return "IMPOSSIBLE"

def solve2(X, V, K, B, T):
    X = list(reversed(X))
    V = list(reversed(V))

    found = set()
    for i in range(len(X)):
        if can_make_it(X[i], V[i], B, T):
            found.add(i)
            if len(found) == K:
                break
    if len(found) < K:
        return "IMPOSSIBLE"
    s = 0
    found = sorted(found)
    for i in range(K):
        s += found[i]-i
    return s
if __name__ == "__main__":
    n = int(raw_input())
    for i in range(1, n+1):
        N, K, B, T = map(int, raw_input().split())
        X = map(int, raw_input().split())
        V = map(int, raw_input().split())
        sol = solve2(X, V, K, B, T)
        #print X, V, K, B, T
        print "Case #%d: %s" % (i, str(sol))
    
        
            
