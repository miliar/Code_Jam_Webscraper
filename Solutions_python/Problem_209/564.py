import heapq
import math

def solve(cakes,k):
    maxSoFar = -1
    for i,c in enumerate(cakes):
        heights = []
        
        for j,h in enumerate(cakes[i + 1:]):
            r,he = h
            currentH = math.pi * he * 2 * r
            if len(heights) < k - 1:
                heapq.heappush(heights, currentH)
            else:
                if len(heights):
                    current = heapq.heappop(heights)
                    if current < currentH:
                        heapq.heappush(heights, currentH)
                    else:
                        heapq.heappush(heights, current)

        #print(heights, len(heights) - k - 1)

        maxSoFar = max(maxSoFar, sum(heights) + math.pi*c[0]*c[1]*2 + math.pi * c[0] * c[0])
        #print(maxSoFar)
    return maxSoFar

for case in range(1, int(input()) + 1):
    n,k = map(int,input().split())
    cakes = []
    for i in range(n):
        r,h = map(int,input().split())
        cakes.append((r,h))
    cakes.sort(reverse=True)
    ans = "{0:.8f}".format(solve(cakes,k))
    print("Case #{}: {}".format(case,ans))