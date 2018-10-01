#!/usr/bin/env python3
import sys

#sys.stdin = open('B-sample.in', 'r')
#sys.stdout = open('B-sample.out', 'w')

for c in range(1, int(input()) + 1):

    a = [int(x) for x in input().strip()]
    n = len(a)
    for i in range(n-1, 0, -1):
        if a[i-1] > a[i]:
            a[i-1] -= 1
            for j in range(i, n):
                a[j] = 9
        #print(a)
    a = ''.join(map(str, a))
    while a[0] == '0':
        a = a[1:]


    print('Case #%s: %s' % (c, a))
