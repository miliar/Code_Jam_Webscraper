import sys, os

def get_triplet(s):
    for a in range(s+1):
        if 0 <= a <= 10:
            for b in range(a-2, a+3):
                if 0 <= b <= 10:
                    c = s - a - b
                    if 0 <= c <= 10 and -2 <= a - c <= 2 and -2 <= b - c <= 2:
                        yield tuple(sorted((a, b, c)))

l = [list(set(get_triplet(s))) for s in range(31)]
init = []
for s, ll in enumerate(l):
    if 2 <= s <= 28:
        a, b, c = ll[0]
        a1, b1, c1 = ll[1]
        if c - a < 2:
            init.append(((a, b, c), (a1, b1, c1)))
        else:
            init.append(((a1, b1, c1), (a, b, c)))
    else:
        init.append(ll[0])
l = init
from pprint import pprint
pprint(l)

def solve(N, S, p, t, m):
    max_result = result = m
    if t:
        for (a, b, c) in l[t[0]]:
            if c - a < 2:
                if max([a,b,c]) >= p:
                    result = solve(N-1, S, p, t[1:], m+1)
                else:
                    result = solve(N-1, S, p, t[1:], m)
            elif S > 0:
                if max([a,b,c]) >= p:
                    result = solve(N-1, S-1, p, t[1:], m+1)
                else:
                    result = solve(N-1, S-1, p, t[1:], m)
            if result > max_result:
                max_result = result
    return max_result

def solve1(N, S, p, t):
    m = 0
    for tt in t:
        if tt < 2:
            if tt >= p:
                m += 1
        elif tt > 28:
            m += 1
        else:
            if max(l[tt][0]) >= p:
                m += 1
            elif max(l[tt][1]) >= p:
                if S > 0:
                    S -= 1
                    m += 1
    return m

input = sys.argv[1]
output = open(os.path.basename(input) + '.out', 'w')
with open(input, 'r') as f:
    for i, line in enumerate(f):
        if not i:
            continue
        line = map(int, line.strip().split())
        N, S, p = tuple(line[:3])
        t = sorted(line[3:])
        output.write('Case #%d: %d\n' % (i, solve1(N, S, p, t)))

output.close()
