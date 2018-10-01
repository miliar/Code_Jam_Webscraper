import heapq

t = int(input())
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    h = []
    heapq.heappush(h, -n)
    for _ in range(k-1):
        elt = -heapq.heappop(h)
        half = int(elt / 2)
        if elt % 2 == 0:
            heapq.heappush(h, -(half - 1))
            heapq.heappush(h, -half)
        else:
            heapq.heappush(h, -half)
            heapq.heappush(h, -half)
    elt = -heapq.heappop(h)
    if elt % 2 == 0:
        maxs = int(elt / 2)
        mins = maxs - 1
    else:
        maxs = int(elt / 2)
        mins = maxs

    print("Case #{}: {} {}".format(i, maxs, mins))

