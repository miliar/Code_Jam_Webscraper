#!/usr/bin/python

for case in range(input()):
    R, k, N = map(int, raw_input().split())
    g = [int(x) for x in raw_input().split()]

    index = zip([-1] * N, [0] * N)
    next = 0
    while index[next][0] == -1:
        c = 0
        for i, p in enumerate(g[next:] + g[:next - len(g)]):
            if c + p <= k:
                c = c + p
            else:
                break
        last = (next + i) % len(g)
        index[next] = (last, c)
        next = last
    cycle_start = next

    cycle_pay = index[cycle_start][1]
    cycle_size = 1
    next = index[cycle_start][0]
    while next != cycle_start:
        cycle_pay = cycle_pay + index[next][1]
        next = index[next][0]
        cycle_size = cycle_size + 1

    next = 0
    pay = 0
    while next != cycle_start and R > 0:
        pay = pay + index[next][1]
        next = index[next][0]
        R = R - 1

    pay = pay + (R / cycle_size) * cycle_pay
    R = R % cycle_size

    next = cycle_start
    while R > 0:
        pay = pay + index[next][1]
        next = index[next][0]
        R = R - 1

    print "Case #%s: %s" % (case + 1, pay)
