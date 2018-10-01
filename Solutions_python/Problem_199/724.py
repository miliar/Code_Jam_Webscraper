#!/usr/bin/env python3

################################################################################

def read_int():
    return int(input())


def read_words():
    return input().split()


def parse(f):
    return [f(x) for x in read_words()]


def read_ints():
    return parse(int)


def read_floats():
    return parse(float)


################################################################################

def flip(p):
    if p == '+':
        return '-'
    if p == '-':
        return '+'
    raise "Impossible"

def solve(p, K):
    i = 0
    f = 0
    S = len(p)
    while i + K <= S:
        if p[i] == '-':
            f += 1
            for j in range(K):
                p[i+j] = flip(p[i+j])
        i += 1

    for j in range(K-1):
        if p[i+j] == '-':
            return "IMPOSSIBLE"

    return f

for C in range(read_int()):
    (p,K) = read_words()
    R = solve([c for c in p],int(K))
    print("Case #{}: {}".format(C + 1, R))
