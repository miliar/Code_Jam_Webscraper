#!/usr/bin/env python
#-*- coding:utf-8 -*-

def dragonseq(n):
    if n == 0:
        while True:
            yield 1
            yield -1
    else:
        g = dragonseq(n-1)
        while True:
            yield 1
            yield g.next()
            yield -1
            yield g.next()

def main():
    fName = 'A-large'
    fIn = open(fName+'.in', 'r')
    fOut = open(fName+'.out', 'w')
    
    def is_light_on(n, k):
        if n == 0: return True
        return k // (2 ** (n-1)) % 2 == 1 and is_light_on(n - 1, k)

    t = int(fIn.readline().strip())

    for i in xrange(t):
        n, k = map(int, fIn.readline().strip().split(' '))
       
        result = 'ON' if is_light_on(n, k) else 'OFF'
        
        #print 'Case #%s (%s): %s\n' % (i + 1, (n, k), result)
        fOut.write('Case #%s: %s\n' % (i + 1, result))
        
if __name__ == '__main__': main()
