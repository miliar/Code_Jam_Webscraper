# Daniel Balle 2017
#
# Bathrooms Stalls
# https://code.google.com/codejam/contest/3264486/dashboard#s=p2

# use this with inverted inputs lol
import heapq

def pee(stalls):
    # find the best stall
    section = -heapq.heappop(stalls) - 1  # minus one since we now poop
    half = section / 2
    if half > 0 : heapq.heappush(stalls, -half)

    if section % 2 == 0:
        if half > 0 : heapq.heappush(stalls, -half)
        return (half, half)

    else:
        heapq.heappush(stalls, -(half+1))
        return (half+1, half)

T = int(raw_input().strip())
for t in range(1, T+1):

    n, k = map(int, raw_input().strip().split(' '))

    stalls = [-n]
    last = None

    for _ in range(k):
        last = pee(stalls)

    print "Case #{}: {} {}".format(t, last[0], last[1])
