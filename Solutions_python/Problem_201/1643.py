from heapq import heappush, heappop

def stall(l, r, k):
    pq = [(-(r - l + 1), l, r)]

    for _ in xrange(k - 1):
        size, l, r = heappop(pq)

        mid = l + (r - l)/2
        rsize = r - mid
        lsize = mid - l

        if lsize > 0:
            heappush(pq, (-lsize, l, mid - 1))
        if rsize > 0:
            heappush(pq, (-rsize, mid + 1, r))

    size, l, r = heappop(pq)
    mid = l + (r - l)/2
    rsize = r - mid
    lsize = mid - l

    return (max(lsize, rsize), min(lsize, rsize))
    

tc = int(raw_input())

for t in xrange(1, tc + 1):
    n, k = map(int, (raw_input().split()))
    res1, res2 = stall(0, n - 1, k)
    print "Case #{}: {} {}".format(t, res1, res2)