# -*- coding: utf-8 -*-
from bisect import bisect_left, bisect_right

lst = set([1, 4, 9])

def is_palindrome(x):
    y = str(x)
    return y == y[::-1]

for i in xrange(1, 2 ** 7):
    x = bin(i)[2:]
    nm = [x + x[::-1], x + x[-2::-1]]
    if x[-1] == '1':
        nm.extend(x[:-1] + '2' + x[-2::-1])
    nm = map(lambda x: int(x) ** 2, nm)
    map(lst.add, filter(is_palindrome, nm))

for i in xrange(25):
    x = '2' + ('0' * i)
    nm = [x + x[::-1], x + '0' + x[::-1], x + '1' + x[::-1]]
    nm = map(lambda x: int(x) ** 2, nm)
    map(lst.add, filter(is_palindrome, nm))

lst = sorted(list(lst))

t = int(raw_input())

for tt in xrange(t):
    a, b = map(int, raw_input().split(' '))
    print 'Case #%s: %s' % (tt + 1, bisect_right(lst, b) - bisect_left(lst, a))

