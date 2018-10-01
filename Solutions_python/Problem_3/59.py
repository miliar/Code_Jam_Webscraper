import psyco
psyco.full()
from math import pi, sqrt, atan2

def pattern_lb(x, y, r, w):
    xx = sqrt(r * r - y * y)
    yy = sqrt(r * r - x * x)
    theta1 = atan2(y, xx)
    theta2 = atan2(yy, x)
    theta = theta2 - theta1
    C = pi * r * r * theta / (2 * pi)
    T1 = (xx - x) * y  / 2.0
    T2 = (yy - y) * x  / 2.0
    return C - T1 - T2

def pattern_lb_rb(x, y, r, w):
    yy1 = sqrt(r * r - (x + w) * (x + w))
    yy2 = sqrt(r * r - x * x)
    theta1 = atan2(yy1, (x + w))
    theta2 = atan2(yy2, x)
    theta = theta2 - theta1
    C = pi * r * r * theta / (2 * pi)
    xx = (x + w) * y / yy1;
    T1 = (xx - x) * y  / 2.0
    T2 = (yy2 - y) * x  / 2.0
    T3 = (x + w - xx) * (yy1 - y)  / 2.0
    return C - T1 - T2 + T3

def pattern_lb_lt(x, y, r, w):
    return pattern_lb_rb(y, x, r, w)

def pattern_lb_rb_lt(x, y, r, w):
    xx = sqrt(r * r - (y + w) * (y + w))
    yy = sqrt(r * r - (x + w) * (x + w))
    return w * w - (x + w - xx) * (y + w - yy) + pattern_lb(xx, yy, r, w)

def inside_circle(x, y, r):
    return sqrt(x * x + y * y) <= r

def cut_ring_area(x, y, w, R, t, f):
    unhit_radius = R - t - f
    lb = inside_circle(x, y, unhit_radius)
    rb = inside_circle(x + w, y, unhit_radius)
    lt = inside_circle(x, y + w, unhit_radius)
    rt = inside_circle(x + w, y + w, unhit_radius)

    if lb and rb and lt and rt:
        return w * w
    elif lb and rb and lt:
        return pattern_lb_rb_lt(x, y, unhit_radius, w)
    elif lb and rb:
        return pattern_lb_rb(x, y, unhit_radius, w)
    elif lb and lt:
        return pattern_lb_lt(x, y, unhit_radius, w)
    elif lb:
        return pattern_lb(x, y, unhit_radius, w)
    elif not (lb or rb or lt or rt):
        return 0.0
    else:
        raise "unknown pattern"


def hit_prob(f, R, t, r, g):
    w = g - 2 * f
    if w <= 0.0:
        return 1.0

    unhit_area = 0.0
    i = 0
    while True:
        x = r + i * (g + 2 * r) + f
        if x > R:
            break

        j = 0
        while True:
            y = r + j * (g + 2 * r) + f
            if y > R:
                break

            ua = cut_ring_area(x, y, w, R, t, f)
            unhit_area += ua
            j += 1

        i += 1

    unhit_area *= 4.0
    racquet_area = pi * R * R
    return (racquet_area - unhit_area) / racquet_area

if __name__ == '__main__':
    N = input()
    for i in range(N):
        f, R, t, r, g = map(lambda s: float(s),
                            raw_input().split(' '))
        print "Case #%d: %f" % (i + 1, hit_prob(f, R, t, r, g))
