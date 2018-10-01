#!/usr/bin/python

def solve(seq):
    t = 0
    s = {'O': [0, 1], 'B': [0, 1]}
    N = int(seq[0])
    for i in range(1, len(seq), 2):
        R = seq[i]
        P = int(seq[i + 1])
        s[R][0] = max(t, s[R][0] + abs(P - s[R][1])) + 1
        s[R][1] = P
        t = max(s['O'][0], s['B'][0])
    return t

T = int(raw_input())
for i in range(T):
    print 'Case #%d: %d' % (i + 1, solve(raw_input().split()))
