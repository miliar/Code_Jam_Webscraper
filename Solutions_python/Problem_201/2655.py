import heapq
import sys


def maxheap_push(h, n):
    heapq.heappush(h, -n)

def maxheap_pop(h):
    return -heapq.heappop(h)

def solve_iter(n, k):
    """Brute force iterative solution"""
    areas = [-n]
    for _ in xrange(k):
        a = maxheap_pop(areas)
        dist_max = a / 2
        dist_min = a - dist_max - 1
        if dist_max == dist_min == 0:
            return (0,0)
        else:
            maxheap_push(areas, dist_max)
            maxheap_push(areas, dist_min)
    return (dist_max, dist_min)

def main():
    t = int(sys.stdin.readline())   

    for case in range(1, t+1):
        n, k = map(int, sys.stdin.readline().split())
        r = solve_iter(n, k)
        print "Case #{}: {} {}".format(case, r[0], r[1])
        

if __name__ == "__main__":
    main()

