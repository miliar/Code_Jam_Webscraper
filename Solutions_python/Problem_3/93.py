import sys
from math import *

def half_circle_strip (radius, height, width):
    return lambda x : min(max(sqrt(max(radius*radius - x*x, 0.0)) - height, 0.0), width)

def integrate(fun, steps, a, b):
    acum = 0.0
    h = (b-a) / steps
    for n in xrange(steps):
        acum += (fun(a + n * h) + fun(a + (n+1) * h)) * h / 2.0
    return acum

def row_safe_area(y, r, g, f, R, t):
    strip = half_circle_strip(R - t -f, y, max(g - 2.0 * f, 0.0))
    x = r + f
    area = 0.0
    areac = 1.0
    while(areac > 0):
        areac = integrate(strip,2000, x, x + max(g - 2.0 * f, 0.0))
        area += areac
        x += g + 2.0 * r
    return area

def safe_area(f, R, t, r, g):
    y = r + f
    area = 0.0
    while(y < R - t - f):
        area += row_safe_area(y, r, g, f, R, t)
        y += g + 2.0 * r
    return area

def probability(f, R, t, r, g):
    return 1.0 - safe_area(f, R, t, r, g) / (pi * R * R / 4.0)

if __name__ == '__main__':
    lines = [l for l in open(sys.argv[1])]
    i = 1
    for l in lines[1:]:
        fl, Rl, tl, rl, gl = [float(n) for n in l.strip().split()]
        print 'Case #%d: %0.6f' % (i, probability(fl, Rl, tl, rl, gl))
        i += 1
