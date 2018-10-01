import sys, math, heapq

lines = open(sys.argv[1], "r").read().splitlines()
res = ""

cases = int(lines[0])

for c in xrange(cases):
    (slots, itr) = map(int, lines[c+1].split(' '))
    # ans = slots / (2 ** (math.log(itr, 2)+1))
    # if slots %2 == 0:
    #     res += "Case #%d: %d %d\n" %(c+1, ans, ans-1)
    # else:
    #     res += "Case #%d: %d %d\n" %(c+1, ans, ans)
    h = [-slots]
    for i in xrange(itr):
        n = -heapq.heappop(h)
        half = int(n/2)
        if n % 2 == 0:
            last = (half, half-1)
            heapq.heappush(h, -half)
            heapq.heappush(h, -(half-1))
        else:
            last = (half, half)
            heapq.heappush(h, -half)
            heapq.heappush(h, -half)
    res += "Case #%d: %d %d\n" %(c+1, last[0], last[1])
open(sys.argv[2], "w").write(res)
