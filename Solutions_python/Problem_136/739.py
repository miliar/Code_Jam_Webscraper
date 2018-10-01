import sys

t = int(sys.stdin.readline())
for c in range(1, t + 1):
    C, F, X = sys.stdin.readline().split()
    C = float(C)
    F = float(F)
    X = float(X)
    time_cost = 0.0
    rat = 2.0
    while True:
        t1 = C / rat
        t = rat * t1 / F
        if rat * (t1 + t) >= X:
            time_cost += X / rat
            break
        rat += F
        time_cost += t1
    print 'Case #%d: %.7f' %(c, time_cost)

