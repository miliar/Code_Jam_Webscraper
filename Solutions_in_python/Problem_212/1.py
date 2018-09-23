from math import *

[t, ] = [int(x) for x in input().split()]

def process_test(num):
    [n, p] = [int(x) for x in input().split()]
    gs = [int(x) % p for x in input().split()]
    xs = [0] * 4
    for i in gs:
        xs[i] += 1

    result = xs[0]
    if p == 2:
        result += ceil(xs[1] / 2)
    elif p == 3:
        pairs = min(xs[1], xs[2])
        xs[1] -= pairs
        xs[2] -= pairs
        result += pairs
        result += ceil(xs[1] / 3) + ceil(xs[2] / 3)
    else:
        pass
    print("Case #", num, ": ", result, sep='')

for num in range(1, t+1):
    process_test(num)