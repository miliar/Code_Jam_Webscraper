#!/usr/bin/env pypy

import sys

def read_f(f):
    s = f.split('.')
    return int(s[0]) * 10000 + int(s[1])

def prob(n, p):
    j = 1
    for i in range(n):
        j *= float(p[i]) / 10000
    return j

def solve(n, p, u):
    while u > 0:
        max_prob = -1.0
        max_i = n
        for i in range(n):
            if p[i] == 10000:
                continue

            p[i] += 1
            m = prob(n, p)
            if m > max_prob:
                max_prob = m
                max_i = i
            p[i] -= 1

        p[max_i] += 1
        u -= 1

    return prob(n, p)

def main():
    s = sys.stdin.readline()
    t = int(s)
    for i in range(t):
        s = sys.stdin.readline()
        n, k = map(int, s.split(' '))
        s = sys.stdin.readline()
        u = read_f(s)
        p = [0] * n
        s = sys.stdin.readline()
        p = list(map(lambda x: read_f(x), s.split()))
        p.sort()
        print("Case #" + str(i + 1) + ": " + str(solve(n, p, u)))

main()
