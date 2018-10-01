#!/usr/bin/env python
#-*- coding:utf-8 -*-

import psyco; psyco.full()

def my_range(p, l):
    for i in xrange(p, l):
        yield i
    for i in xrange(0, p):
        yield i

def perfect(K):
    d = [0] * K
    mmap = range(K)
    p2 = 0
    for i in xrange(K):
        p2 = (i + p2) % K
        p1 = mmap.pop(p2)
        
        K -= 1
        d[p1] = i+1
        
    return d

def result(K, inputs):
    p = perfect(K)
    return ' '.join(map(str, [p[i-1] for i in inputs]))

def test():
    pass

if __name__ == '__main__':
    from sys import argv, exit
    if len(argv) < 2:
        test()
        exit()
    
    file_name = argv[1]
    lines = open(file_name).read().split('\n')[0:-1]
    nb_inputs = int(lines[0])
    lines = lines[1:].__iter__()
    
    for n in range(nb_inputs):
        K = int(lines.next())
        inputs = map(int, lines.next().split(' '))[1:]
        print 'Case #%s:' % (n+1), result(K, inputs)

