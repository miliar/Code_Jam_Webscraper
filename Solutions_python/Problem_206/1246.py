from __future__ import division

T = int(input())
for TC in range(1, T + 1):
    case = raw_input().split()
    D = int(case[0])
    N = int(case[1])
    res = 0
    for n in range(N):
        horse = raw_input().split()
        K_i = int(horse[0])
        S_i = int(horse[1])
        spd = (D - K_i) / S_i
        res = max(res, spd)
    print("Case #%d: %.6f" % (TC, D / res))