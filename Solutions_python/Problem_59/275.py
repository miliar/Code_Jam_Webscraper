#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(N, foo):
        res = []
        for _ in xrange(N):
                res.append(foo())
        return res
def readlinearray(foo): return map(foo, raw_input().split())

def create(dirs, root):
    count = 0
    for d in dirs:
        parts = [v for v in d.split('/') if v]
        
        current = root
        for p in parts:
            if p not in current:
                current[p] = {}
                count += 1
            current = current[p]
    
    return count

def get_nmkdirs(dirs, ndirs):
    
    root = {}
    create(dirs, root)
    return create(ndirs, root)

if __name__ == '__main__':
    T = readint()
    for t in xrange(1, T+1):
        N, M = readlinearray(int)
        
        dirs = []
        for _ in xrange(N):
            dirs.append(raw_input())

        ndirs = []
        for _ in xrange(M):
            ndirs.append(raw_input())
        
        ans = get_nmkdirs(dirs, ndirs)
        print 'Case #%d: %s' % (t, ans)
