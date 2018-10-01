#!/usr/bin/env python
# -*- coding:utf-8 -*-

def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(N, foo):
        res = []
        for _ in xrange(N):
                res.append(foo())
        return res
def readlinearray(foo): return map(foo, raw_input().split())

def get(s_max, members):
    np = 0
    nc = 0
    for idx, v in enumerate(members):
        nc += max(0, idx - (np + nc))
        np += v
    return nc

if __name__ == '__main__':
    T = readint()
    for t in xrange(1, T+1):
        s_max, members_str = raw_input().split()
        s_max = int(s_max)
        members = map(int, list(members_str))
        ans = get(s_max, members)
        print 'Case #%d: %d' % (t, ans)