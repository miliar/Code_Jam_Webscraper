def solve(A, B, K):
    cpt = 0
    for i in range(A):
        for j in range(B):
            if (i&j) < K:
                cpt += 1
    return cpt

T = int(raw_input())
for t in range(T):
    sol = solve(*map(int, raw_input().split()))
    print "Case #{}: {}".format(t+1, sol)
