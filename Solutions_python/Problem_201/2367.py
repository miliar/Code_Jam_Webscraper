import Queue
import heapq

def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n, k = [int(s) for s in raw_input().split(" ")]
        y, z = bathroomStalls(n ,k)
        print "Case #{}: {} {}".format(i, y, z)

# def bathroomStalls(n, k):
#     if n == k: return 0, 0
#     stalls = Queue.PriorityQueue(n)
#     stalls.put((-n, n))
#     openStalls, newStalls, otherStalls = 0, 0, 0
#     for i in xrange(0, k, 1):
#         openStalls = stalls.get()[1] - 1
#         newStalls = openStalls//2
#         otherStalls = openStalls-newStalls
#         stalls.put((-otherStalls, otherStalls))
#         stalls.put((-newStalls, newStalls))
#
#     return otherStalls, newStalls


def bathroomStalls(n, k):
    if n == k: return 0, 0
    stalls = []
    heapq.heappush(stalls, (-n, n))
    openStalls, newStalls, otherStalls = 0, 0, 0
    for i in xrange(0, k, 1):
        openStalls = heapq.heappop(stalls)[1] - 1
        newStalls = openStalls//2
        otherStalls = openStalls-newStalls
        heapq.heappush(stalls, (-otherStalls, otherStalls))
        heapq.heappush(stalls, (-newStalls, newStalls))

    return otherStalls, newStalls

main()