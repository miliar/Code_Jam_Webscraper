def solve(n, k):
    level = k.bit_length() - 1
    lo = [0, n]
    hi = [1, n]
    for i in range(level):
        #print(hi, lo)
        l = 0
        h = 0
        if hi[0] > 0:
            if hi[1] & 1 == 1:
                h += hi[0] * 2
            else:
                l += hi[0]
                h += hi[0]
        if lo[0] > 0:
            if lo[1] & 1 == 1:
                l += lo[0] * 2
            else:
                l += lo[0]
                h += lo[0]
        hi[0] = h
        lo[0] = l
        hi[1] = (hi[1]) >> 1
        lo[1] = (lo[1] - 1) >> 1
    c = hi[1] if k - (1 << level) < hi[0] else lo[1]
    return (c >> 1, (c - 1) >> 1)


#solve(1000, 511)
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    result = solve(n, k)
    print('Case #%d: %d %d' % (i + 1, result[0], result[1]))
