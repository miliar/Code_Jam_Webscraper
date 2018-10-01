__author__ = 'Servy'

import sys

maxFarms = 2 ** 32

def solve(c, f, x):
    time = 0
    speed = 2

    nopTime = x / speed
    buyTime = c / speed + (x / (speed + f))

    while buyTime < nopTime:
        time += c / speed
        speed += f

        nopTime = x / speed
        buyTime = c / speed + (x / (speed + f))

    return time + nopTime

testNumber = int(sys.stdin.readline().strip())
for test in range(1, testNumber + 1):
    (c, f, x) = map(float, sys.stdin.readline().split())
    print("Case #%d: %.7f" % (test, solve(c, f, x)))