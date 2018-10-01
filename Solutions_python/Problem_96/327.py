import math

def solve(N, S, p, t):
    count = 0
    for total in t:
        best = math.ceil(total / 3)
        if best >= p:
            count += 1
        elif best == p - 1 and S > 0 :
            if total % 3 != 1 and total != 0: 
                count += 1
                S -= 1
    return count

T = int(input())
for i in range(1, T + 1):
    N, S, p, *t = map(int, input().split())
    print("Case #%d: %s" % (i, solve(N, S, p, t)))
