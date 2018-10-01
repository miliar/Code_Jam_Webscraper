#!/usr/bin/python
import sys
di = {}
di['/'] = 1

total = 0

def add_di(path):
    if not di.has_key(path):
        di[path] = 1
    l = path.split('/')
    st = ''
    for i in l:
        st += i
        st += '/'
        if not di.has_key(st):
            di[st] = 1

def mk_di (path):
    op = 0
    if di.has_key(path):
        return op

    l = path.split('/')
    st = ''
    for i in l:
        st += i
        st += '/'
        if not di.has_key(st):
            op += 1
            di[st] = 1

    return op
    

n = int(sys.stdin.next())

for i in xrange(n):
    di.clear()
    total = 0
    di['/'] = 1
    para = map(int, sys.stdin.next().strip().split(" "))

    for j in xrange(para[0]):
        de = sys.stdin.next().strip()
        add_di(de)

    for j in xrange(para[1]):
        dc = sys.stdin.next().strip()
        total += mk_di (dc)
        
    print "Case #%d: %d" % ( i + 1, total)
            
            
    
        
        
