# usage:  (py3 a.py < a.in) > a.out

import time, sys, inspect
from itertools import combinations

lineno = lambda: inspect.currentframe().f_back.f_back.f_lineno
print = lambda *a, **k: __builtins__.print(str(lineno())+':', *a, file=sys.stderr, **k)
map = lambda *a: list(__builtins__.map(*a))
reversed = lambda *a: list(__builtins__.reversed(*a))

#---------------------------------------------

'''
side condition means we always fill the biggest gap
    then break ties by leftmostedness
'''

import math

def run(data):
    n, k = data
    ret = n

    for c in reversed(str(bin(k))[3:]):
        if c == '0':
            ret = math.ceil((ret-1)/2)
        else:
            ret = math.floor((ret-1)/2)

    return str(math.ceil((ret-1)/2)) + ' ' + str(math.floor((ret-1)/2))

#---------------------------------------------

def read_case():
    return [int(k) for k in list(input().split())]

for i in range(int(input())):
    outstr = 'Case #'+str(i+1)+': '+str(run(read_case()))
    print(outstr, ' @ t =', time.clock())
    __builtins__.print(outstr)
