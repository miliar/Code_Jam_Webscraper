import math

def function(pancakes, N, K):
    # pancakes = [[R, H], ...]
    pancakes = sorted(pancakes, key=lambda x:x[0], reverse=True)
    maxx = 0.
    for pancake in xrange(N - K + 1):
        stack = [[p[0], p[1], p[0] * p[1]] for p in pancakes[pancake+1:]]
        stack = sorted(stack, key=lambda x:x[2], reverse=True)
        surface = math.pi * pancakes[pancake][0] ** 2 + 2. * math.pi * pancakes[pancake][0] * pancakes[pancake][1]
        for i in xrange(0, K-1):
            surface = surface + 2. * math.pi * stack[i][2]
        if surface > maxx:
            maxx = surface
    return maxx

T = int(raw_input().strip())  # read a line with a single integer

for i in xrange(1, T + 1):
    N, K = map(int, raw_input().strip().split(' '))  # read input
    pancakes = []
    for j in xrange(N):
        pancakes.append(map(float, raw_input().strip().split(' ')))
    x = function(pancakes, N, K)
    print "Case #{:d}: {:.6f}".format(i, x)
