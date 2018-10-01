#/usr/bin/cython --embed -2 C.pyx
#/usr/bin/gcc -o C -I/usr/include/python2.7 C.c /usr/lib/libpython2.7.so
#./C

import sys, math

cdef int reverse(int v):
    cdef r = 0
    while v > 0:
        r = r * 10 + v % 10
        v /= 10
    return r
   

cdef int p7[20000]
cdef int i, j, p7c, c, c1, c2

p7c = 0
for c in range(1, 8):
    c2 = 10 ** ((c+1)/2)
    c1 = c2 / 10
    
    for i in range(c1, c2):
        if c % 2 == 1:
            p7[p7c] = i * c1 + reverse(i / 10)
        else:
            p7[p7c] = i * c2 + reverse(i)

        #print >>sys.stderr, p7[p7c]
        p7c += 1
        
print >>sys.stderr, p7c

cdef ispalindromes(long v):
    cdef int vv[20]
    cdef int i, c
    c = 0
    while v>0:
        vv[c] = v % 10
        v /= 10
        #print >>sys.stderr, vv[c],
        c += 1
    #print >>sys.stderr, ''
    for i in range(c/2):
        if vv[i] != vv[c-i-1]: return False
    return True

cdef int q():
    cdef long a, b, v
    cdef int a2, b2, i, c
    global p7, p7c
    a, b = map(long, sys.stdin.readline().split())
    a2 = int(math.sqrt(a))
    b2 = int(math.sqrt(b))+1
    
    c = 0
    for i in range(p7c):
        if p7[i]<a2: continue
        if p7[i]>b2: break
        v = p7[i]
        v *= v
        if v<a: continue
        if v>b: break
        if ispalindromes(v): 
            #print >>sys.stderr, v
            c += 1
    #print >>sys.stderr, '--', c
    return c

T = int(sys.stdin.readline())
for t in range(T):
    print 'Case #%d: %d' % (t+1, q())
    