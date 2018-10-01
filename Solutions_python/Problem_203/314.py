# -*- coding: utf-8 -*-
"""
@author: jmzhao
GCJ 2017 Round 1A
"""

from itertools import product
import sys

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
    
def once():
    '''to cope once'''
    r, c =IO.gets(int)
    a = [list(IO.get()) for _ in range(r)]
    for i, j in product(range(r), range(c-1)) :
        if a[i][j] is not '?' and a[i][j+1] is '?' :
            a[i][j+1] = a[i][j]
    for i, j in product(range(r), reversed(range(c-1))) :
        if a[i][j+1] is not '?' and a[i][j] is '?' :
            a[i][j] = a[i][j+1]
    for j, i in product(range(c), range(r-1)) :
        if a[i][j] is not '?' and a[i+1][j] is '?' :
            a[i+1][j] = a[i][j]
    for j, i in product(range(c), reversed(range(r-1))) :
        if a[i+1][j] is not '?' and a[i][j] is '?' :
            a[i][j] = a[i+1][j]
    return a

def show(ans) :
    return '\n' + '\n'.join(''.join(line) for line in ans)
    
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
