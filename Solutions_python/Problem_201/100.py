#!/usr/local/bin/python
import sys
import heapq

def solve():
    line = sys.stdin.readline().strip()
    N, K = line.split()
    N = int(N)
    K = int(K)

    rangeCount = dict()
    rangeCount[N] = 1
    rangeList = []
    heapq.heappush(rangeList, -N)

    while len(rangeList) > 0:
        # Pop the largest range from the heap
        largestRange = -heapq.heappop(rangeList)
        numRanges = rangeCount.pop(largestRange)

        # Calculate how this range would be split
        leftRange = largestRange / 2
        rightRange = (largestRange-1) / 2

        # If the last range to be split would be one of these, return
        if numRanges >= K:
            return "{} {}".format(leftRange, rightRange)

        K -= numRanges 
        if leftRange not in rangeCount:
            rangeCount[leftRange] = numRanges
            heapq.heappush(rangeList, -leftRange)
        else:
            rangeCount[leftRange] += numRanges
        if rightRange not in rangeCount:
            rangeCount[rightRange] = numRanges
            heapq.heappush(rangeList, -rightRange)
        else:
            rangeCount[rightRange] += numRanges
    return None

cases = int(sys.stdin.readline())
for case in range(cases):
    print "Case #{}: {}".format(case+1, solve())
