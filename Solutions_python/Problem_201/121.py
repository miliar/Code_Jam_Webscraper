def allocate(s, c, stalls):
    # print "key: %d" % s
    # print("stall: %s" % str(stalls))
    stalls.pop(s)
    if s % 2 == 1:
        d = stalls.get((s - 1) / 2)
        if d is not None:
            stalls[(s - 1) / 2] = d + c * 2
        else:
            stalls[(s - 1) / 2] = c * 2
        return (s - 1) / 2, (s - 1) / 2
    else:
        d1 = stalls.get(s / 2)
        d2 = stalls.get(s / 2 - 1)
        if d1 is not None:
            stalls[s / 2] = d1 + c
        else:
            stalls[s / 2] = c
        if d2 is not None:
            stalls[s / 2 - 1] = d2 + c
        else:
            stalls[s / 2 - 1] = c
        return s / 2, s / 2 - 1


def solve(n, k):
    count = 0
    stalls = {n: 1}
    while k > count:
        keys = sorted(stalls.keys(), reverse=True)
        for s in keys:
            c = stalls.get(s)
            if count + c >= k:
                return allocate(s, c, stalls)
            else:
                count += c
                allocate(s, c, stalls)
    return 0, 0

t = int(raw_input())

for i in range(1, t + 1):
    n, k = map(int, raw_input().strip().split())
    print("Case #%d: " % i + "%d %d" % solve(n, k))
