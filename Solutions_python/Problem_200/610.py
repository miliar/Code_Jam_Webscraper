#!/usr/bin/python
import re
import inspect
from sys import argv, exit


def rstr():
    return input()


def rstrs(splitchar=' '):
    return [i for i in input().split(splitchar)]


def rint():
    return int(input())


def rints(splitchar=' '):
    return [int(i) for i in rstrs(splitchar)]


def varnames(obj, namespace=globals()):
    return [name for name in namespace if namespace[name] is obj]


def pvar(var, override=False):
    prnt(varnames(var), var)


def prnt(*args, override=False):
    if '-v' in argv or override:
        print(*args)


tidy = {}


def is_tidy(i):
    s = str(i)
    old_c = s[0]
    old_index = 0
    for j, c in enumerate(s):
        if j == 0:
            continue
        if ord(c) < ord(old_c):
            unmod = s[:old_index]
            decced = chr(ord(old_c) - 1)
            nines = '9' * (len(s[j:]))
            return False, int(unmod + decced + nines)
        old_c = c
        old_index = j
    return True, -1


def get_sol(mx):
    while mx >= 1:
        mx_tidy, next = is_tidy(mx)
        if mx_tidy:
            return mx
        mx = int(next)


if __name__ == '__main__':
    n = rint()
    for i in range(n):
        mx = rint()
        sol = get_sol(mx)
        print('Case #{}: {}'.format(i + 1, sol))
