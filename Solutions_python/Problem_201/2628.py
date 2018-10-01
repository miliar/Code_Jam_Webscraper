from math import ceil
import heapq

fileName = 'C-small-1-attempt0'

with open('%s.in' % fileName, 'r') as f, open('%s.out' % fileName, 'w') as g:
    T = int(f.readline())
    for t in range(1, T+1):
        N, people = map(lambda x: int(x), f.readline().strip().split(' '))
        if people == N:
            maxDist, minDist = 0, 0
        else:
            occupied = [(-N, 0, N+1)]
            for p in range(people):
                pair = heapq.heappop(occupied)
                stall = pair[1] + int(ceil(-pair[0]/2))
                leftHalfMaxDist = stall - pair[1] - 1
                if leftHalfMaxDist > 0:
                    left = (-leftHalfMaxDist, pair[1], stall)
                    heapq.heappush(occupied, left)
                rightHalfMaxDist = pair[2] - stall - 1
                if rightHalfMaxDist > 0:
                    right = (-rightHalfMaxDist, stall, pair[2])
                    heapq.heappush(occupied, right)
            maxDist = max(leftHalfMaxDist, rightHalfMaxDist)
            minDist = min(leftHalfMaxDist, rightHalfMaxDist)
        g.write('Case #%d: %d %d\n' %(t, maxDist, minDist))
