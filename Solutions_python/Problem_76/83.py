

def solve(cs):
    x = 0
    tot = 0
    smallest = 0
    for c in cs:
        x ^= c
        tot += c
        smallest = c if smallest == 0 else min(smallest, c)
    if x != 0:
        return 0
    else:
        return tot-smallest


T = int(raw_input())

for t in xrange(1, T+1):
    raw_input()
    cs = (int(w) for w in raw_input().split())
    solution = solve(cs)
    print 'Case #%d: %s' % (t, 'NO' if solution == 0 else str(solution))

