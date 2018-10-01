#!/usr/bin/env python2


def main():
    n = int(raw_input())
    for i in xrange(n):
        items = raw_input()
        s, n = items.split()
        result = brute_force2(s, int(n))
        print 'Case #{0}: {1}'.format(i+1, result)


def brute_force2(s, n):
    flipping = '-'
    flips = 0
    s = [c for c in s]
    for i in xrange(len(s)-(n-1)):
        #print i, s[i], ''.join(s)
        if s[i] == flipping:
            flips += 1
            flip2(s, i, n)
    for i in xrange(1+(len(s)-n), len(s)):
        if s[i] == flipping:
            return 'IMPOSSIBLE'
    return str(flips)


def flip2(s, i, n):
    for i in xrange(i, i+n):
        s[i] = '-' if s[i] == '+' else '+'


def brute_force(s, n):
    flipping = '-'
    flips = 0
    for i in xrange(len(s)-(n-1)):
        #print i, s[i], s
        if s[i] == flipping:
            flips += 1
            s = flip(s, i, n)
    for i in xrange(1+(len(s)-n), len(s)):
        if s[i] == flipping:
            return 'IMPOSSIBLE'
    return str(flips)


def flip(s, i, n):
    news = s[:i] if i > 0 else ''
    for idx in range(i, i+n):
        news += '-' if s[idx] == '+' else '+'
    news += s[i+n:] if i+n < len(s) else ''
    return news

if __name__ == '__main__':
    main()
