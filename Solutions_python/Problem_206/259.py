# Steed 2: Cruise Control

def solve(d, n, ks):
    t = 0
    for (k, s) in ks:
        t = max(t, (d - k) * 1.0 / s)
    return d / t

cases = int(raw_input())
for case in range(1, cases + 1):
    (d, n) =  map(int, raw_input().split(' '))
    ks     = [map(int, raw_input().split(' ')) for x in range(n)]
    print "Case #" + str(case) + ": " + str(solve(d, n, ks))
