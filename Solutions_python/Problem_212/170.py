import math

def solve():
    N, P = (int(x) for x in input().split())
    G = [int(x) % P for x in input().split()]
    R = [G.count(x) for x in range(P)]
    if P == 2:
        return R[0] + R[1] // 2 + R[1] % 2
    elif P == 3:
        if R[1] == R[2]:
            return R[0] + R[1]
        elif R[1] > R[2]:
            return R[0] + R[2] + (R[1] - R[2] + 2) // 3
        else: # R[1] < R[2]
            return R[0] + R[1] + (R[2] - R[1] + 2) // 3
    elif P == 4:
        if R[1] == R[3]:
            return R[0] + R[1] + R[2] // 2 + R[2] % 2
        elif R[1] > R[3]:
            r = R[0] + R[3] + R[2] // 2
            r1 = R[1] - R[3]
            if R[2] % 2 == 1:
                r += 1
                r1 -= 2
            if r1 > 0:
                r += (r1 + 3) // 4
            return r
        else: # R[1] < R[3]
            r = R[0] + R[1] + R[2] // 2
            r3 = R[3] - R[1]
            if R[2] % 2 == 1:
                r += 1
                r3 -= 2
            if r3 > 0:
                r += (r3 + 3) // 4
            return r

T = int(input())
for t in range(1, T + 1):
    print ("Case #%d: %d" % (t, solve()))
