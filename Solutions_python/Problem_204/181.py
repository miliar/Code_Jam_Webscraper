from itertools import product
from math import ceil, floor

def solve(N, P, R, Q):
    def cook_range(x):
        return (int(ceil(float(x) / 1.1)), int(floor(float(x) / 0.9)))

    new_Q = [[] for i in range(N)]
    for i, j in product(range(N), range(P)):
        Q[i][j] = float(Q[i][j]) / R[i]
        a, b = cook_range(Q[i][j])
        if a <=b: new_Q[i].append(Q[i][j])
    Q = new_Q

    res = 0
    for t in range(P):
        num_ingred = 0
        for i in range(N):
            if len(Q[i]) == 0: return res
            a, b = cook_range(Q[i][0])
            num_ingred = max(num_ingred, a)
        all_ok_flags = True
        for i in range(N):
            while True:
                if len(Q[i]) == 0: return res
                a, b = cook_range(Q[i][0])
                if b < num_ingred: Q[i] = Q[i][1:]
                elif a <= num_ingred <= b: break
                elif num_ingred < b: all_ok_flags = False
            if all_ok_flags == False:
                break
        if all_ok_flags == True:
            res += 1
            for i in range(N):
                Q[i] = Q[i][1:]
    return res

T = input()
for t in range(1, T + 1):
    Ingred = []
    N, P = map(int, raw_input().split())
    R = map(int, raw_input().split())
    Q = []
    for p in range(N):
        Q.append(sorted(map(int, raw_input().split())))
    print 'Case #%d: %d'%(t, solve(N, P, R, Q))
