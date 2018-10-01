#!/usr/bin/env python

import math, sys

def circintegral(u, a):
    """Returns integral sqrt(a^2 - u^2) du"""
    return u / 2.0 * math.sqrt(a**2 - u**2) + \
        a ** 2 / 2.0 * math.asin(u / a)

def square_circ_area(r, x0, x1, y):
    extra = 0

    top = math.sqrt(r ** 2 - x0 ** 2)
    if y + (x1 - x0) < top:
        topy = y + (x1 - x0)
        topx = math.sqrt(r ** 2 - topy ** 2)
        assert topx < x1
        extra += circintegral(topx, r) - circintegral(x0, r) - topy * (topx - x0)
    
    right = math.sqrt(r ** 2 - y ** 2)
    if x1 > right:
        x1 = right

    extra += y * (x1 - x0)

    assert x0 < x1 <= r
    assert x0 > 0
    assert y > 0
    return circintegral(x1, r) - circintegral(x0, r) - extra

def in_circle(r, x, y):
    return x ** 2 + y ** 2 <= r ** 2

def solve(f, R, t, r, g):
    area = 0.0
    a = R - t - f
    d = g - f
    step = g + 2.0 * r
    x = r
    square_area = (g - 2.0 * f) ** 2

    if g <= 2.0 * f:
        return 1.0

    assert f < d

    while x < a:
        y = r
        while y < a:
            if not in_circle(a, x + f, y + f):
                break
            if in_circle(a, x + d, y + d):
                area += square_area
            else:
                area += square_circ_area(a, x + f, x + d, y + f)
            y += step
        x += step
            
    area *= 4.0

    return 1.0 - (area / (math.pi * R ** 2))

readline = lambda : sys.stdin.readline().strip()

N = int(readline())

for n in range(N):
    line = map(float, readline().split())
    print "Case #%d: %.6f" % (n+1, solve(*line))
