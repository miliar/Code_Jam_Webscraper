#!/usr/bin/python3

import sys

def cmp(a, b):
    return (a > b) - (a < b)

def solve(y, m, b):
    # solve for x
    # y = mx + b
    return (y - b) / m

for i in range(int(input())):
    i += 1
    zeit = 0.0
    rate = 2.0
    cost, bonus, target = map(float, input().split())
    if target < cost:
        print("Case #%d: %.7f" % (i, target / rate))
        continue
    eq1 = [target, rate, cost]
    eq2 = [target, rate + bonus, 0]
    zeit += cost / rate
    while True:
        zeit1, zeit2 = solve(*eq1), solve(*eq2)
        res = cmp(zeit1, zeit2)
        if res == 1:
            # eq1 > eq2 we should buy a factory
            #print("buying factory")
            eq1[1] += bonus
            eq2[1] += bonus
            #print(zeit, '+', (cost / (eq1[1])))
            zeit += (cost / (eq1[1]))
        elif res == -1:
            # eq1 < eq2 don't buy a factory
            #print("don't buy factory")
            #print(zeit, "->", zeit + zeit1)
            zeit += zeit1
            break
        else:
            zeit += zeit1
            break
    print("Case #%d: %.7f" % (i, zeit))
