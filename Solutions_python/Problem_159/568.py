# coding=utf-8

import time
import math

inPath = "/home/md/Downloads/A-large.in"

num = lambda: nums()[0]
nums = lambda: [int(word) for word in words()]
matrix = lambda r: [nums() for _ in range(r)]
words = lambda: line().split()
lines = lambda n: [line() for _ in range(n)]
line = lambda: fin.readline().rstrip()
write = lambda f, s, *args: f.write(s.format(*args))


def main():
    global fin
    out = inPath.split(".")[0] + ".out"
    with open(inPath) as fin:
        with open(out, "w") as outFile:
            start = time.time()

            T = num()
            for x in xrange(1, T + 1):
                write(outFile, "Case #{}: {}\n", x, solve())

            end = time.time()
            print("Solved in {:f} sec".format((end - start)))


def solve():
    N = num()
    M = nums()

    method1 = 0
    max_diff = 0

    for i in xrange(1, N):
        eaten = M[i-1] - M[i]
        if eaten > 0:
            method1 += eaten
            if max_diff < eaten:
                max_diff = eaten

    speed2 = max_diff
    method2 = 0

    for i in xrange(1, N):
        method2 += min(speed2, M[i-1])

    return "{} {}".format(method1, method2)


main()
