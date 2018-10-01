# -*- coding: utf-8 -*-
"""
@author: jmzhao
GCJ 2017 Round 1B
"""

from itertools import product, permutations
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
    n, R, O, Y, G, B, V = IO.gets(int)
    
    s = ''
    d = dict(zip('RYB', [R,Y,B]))
    a, b, c = map(lambda x : x[0], sorted(d.items(), key=lambda x : x[1]))
    while True :
        if d[a] + d[b] > d[c] :
            s += a + b + c
            d[a] -= 1
            d[b] -= 1
            d[c] -= 1
        elif d[a] > 0 :
            s += a + c
            d[a] -= 1
            d[c] -= 1
        elif d[b] > 0 :
            s += b + c
            d[b] -= 1
            d[c] -= 1
        elif d[c] > 0 :
            return
        else :
            break
    return s
            

def show(ans) :
    return ans if ans else 'IMPOSSIBLE' #IO.tostr(ans, writer=str, delim=' ')
    
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
