# -*- coding: utf-8 -*-
"""
@author: jmzhao
GCJ 2017 Round 1B
"""

import sys
from collections import Counter
from math import ceil

class IO :
    def get(reader=str) :
        return reader(input().strip())
    def gets(reader=str, delim=None) :
        return [reader(x) for x in input().strip().split(delim)]
    def tostr(raw, writer=str, delim=' ') :
        return delim.join(writer(x) for x in raw)

def prework(argv):
    '''do something according to argv,
    return a message describing what have been done.'''
    pass

def mmm(a, b) :
    return max(a,b) - min(a,b)

def once():
    n, p = IO.gets(int)
    gs = IO.gets(int)
    c = Counter(g % p for g in gs)
    if p == 2 :
        return c[0] + ceil(c[1]/2)
    elif p == 3 :
        return c[0] + min(c[1], c[2]) + ceil(mmm(c[1], c[2])/3)
    elif p == 4 :
        return c[0] + ceil(c[2]/2) + min(c[1], c[3]) + ceil((mmm(c[1], c[3]) + c[2] % 2) / 4)

def show(ans) :
    return ans #IO.tostr(ans, writer=str, delim=' ')
    
def printerr(*v):
    print(*v, file=sys.stderr)

def main():
    TT = IO.get(int)
    for tt in range(1,TT+1):
        printerr("coping Case %d.."%(tt))
        ans = once()
        print("Case #%d: %s"%(tt, show(ans)))

if __name__ == '__main__' :
    msg = prework(sys.argv)
    print("prework done with", msg, file=sys.stderr)
    main()
