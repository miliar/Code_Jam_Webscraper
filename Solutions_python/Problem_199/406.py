#!/usr/bin/env python

from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(1500)


def flip(stack, flipper):
    for i in range(flipper):
        stack[i] = '+' if stack[i] == '-' else '-'
    return stack


def flips(stack, flipper):
    try:
        i = stack.index('-')
        stack = stack[i:]
        if len(stack) < flipper:
            return "IMPOSSIBLE"
        stack = flip(stack, flipper)
        res = flips(stack, flipper)
        return 1 + res if type(res) == int else res
    except ValueError:
        return 0


def solve(stack, flipper):
    stack = list(stack)
    flipper = int(flipper)
    return flips(stack, flipper)


cases = int(stdin.readline())
for case in xrange(cases):
    s, k = stdin.readline().split()
    stdout.write("Case #%d: %s\n" % (case+1, str(solve(s, k))))
