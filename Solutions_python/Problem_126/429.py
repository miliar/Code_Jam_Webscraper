#!/usr/bin/python

import re

cases = int(input())
for case in range(1, cases + 1):
    name, n = input().split()
    n = int(n)
    nValue = 0
    prevMatch = -1
    for m in re.finditer(r'(?=([^aeiou]{%s}))' % n, name):
        left = m.start() - prevMatch
        right = len(name) - m.start() - n + 1
        nValue += left * right
        prevMatch = m.start()
    print('Case #{}: {}'.format(case, nValue))
