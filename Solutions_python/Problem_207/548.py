import sys

idx_map = {'R':0, 'Y': 1, 'B':2 }

def solve(R, Y, B):
    maxN = max (R, Y, B)

    #print R, Y, B, maxN

    if maxN > (R + Y + B - maxN):
        return "IMPOSSIBLE"

    numbers = [R, Y, B]
    maxColor = 'R'

    if Y == maxN:
        maxColor = 'Y'

    if B == maxN:
        maxColor = 'B'

    ans = ""
    remaining = maxN
    for i in xrange(maxN):
        ans += maxColor
        numbers[idx_map[maxColor]] -= 1

        done = False
        for c, idx in idx_map.iteritems():
            #print c, idx, remaining
            if c == maxColor:
                continue
            if numbers[idx] == remaining:
                ans += c
                numbers[idx] -= 1
                #print c, idx, remaining, ans
                done = True
            elif numbers[idx] > 0 and not done:
                ans += c
                numbers[idx] -= 1
                #print c, idx, remaining, ans
                done = True
        remaining -= 1

    return ans

T = int(raw_input())

for tc in xrange(1, T + 1):
    numbers = map(int, raw_input().split())

    N = numbers[0]
    numbers = numbers[1:]

    ans = solve(numbers[0], numbers[2], numbers[4])
    print "Case #%d: %s" % (tc, ans)
