#!/usr/local/bin/python

import sys

baseF = 2.0

def t_farm(C, F, n):
    if n < 1:
        return 0.0

    t = C / baseF

    for i in range(1, n):
        t += C / (i * F + baseF)

    return t

def cookies(n):
    if n == 0:
        return lambda C, F, t: baseF * t

    cookies_n_1 = cookies(n - 1.0)

    def g(C, F, t):
        if (t <= t_farm(C, F, n)):
            return cookies_n_1(C, F, t)
        return (n * F + baseF) * t - (n * F + baseF) * t_farm(C, F, n)

    return g

def cmp(epsilon):
    def g(a, b):
        if (abs(a -b) <= epsilon):
            return 0.0
        if (a < b):
            return -1.0
        return 1
    return g

def lin_search_inverse(f, C, F, Y, cmp, x0):
    #print "starting zigzag for", C, F, Y, "from", x0, "->", f(C, F, x0)
    x = x0
    y = f(C, F, x)
    c = cmp(y, Y)
    eps = 1.0
    direction = 1.0

    while c != 0:
        if c == 1:
            direction = -1.0
            eps /= 2

        x += direction * eps
        y = f(C, F, x)
        #print "test", x, "->", y, "at", eps
        c = cmp(y, Y)

    return x



def bin_search_inverse(C, F, Y, n, comp, x0, x1):
    # x0=x0 or 0.0
    # x1=Y
    f = cookies(n)
    x = x0 + (x1 - x0) / 2.0
    y = f(C, F, x)
    c = comp(y, Y)

    while c != 0:
        if c == 1:
            x1 = x
        else:
            x0 = x

        if x0 == x1:
            return x

        x = x0 + (x1 - x0) / 2.0
        y = f(C, F, x)
        c = comp(y, Y)
        #print "testing ", C, F, Y, n, x0, x1, x, y

    return x

def find_min_farms_t(C, F, Y):
    farms = 0
    time = 99999999

    while True:
        # inverse for last slope
        t = (Y + (farms * F + baseF) * t_farm(C, F, farms)) / (farms * F + baseF)
        # look
        if t >= time:
            break

        time = t
        farms += 1

    return time




if len(sys.argv) < 2:
    print 'give file'
    exit(1)

file = open(sys.argv[1])

tests = file.readline()

for i in range(1, int(tests) + 1):
    vs = file.readline().split(' ')
    t = find_min_farms_t(float(vs[0]), float(vs[1]), float(vs[2]))

    print "Case #" + str(i) + ":", round(t, 7)