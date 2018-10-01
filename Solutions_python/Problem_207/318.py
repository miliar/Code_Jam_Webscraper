#!/usr/bin/env python

label = ['R', 'Y', 'B']
for nnn in xrange(1, int(raw_input())+1):
    print "Case #%d:" % (nnn),
    N, R, O, Y, G, B, V = [int(x) for x in raw_input().split()]
    num = [R, Y, B]
    argmax = 0
    for i in xrange(3):
        if num[i] > num[argmax]:
            argmax = i
    if 2*num[argmax] > N:
        print 'IMPOSSIBLE'
    else:
        i, j, k = argmax, (argmax+1)%3, (argmax+2)%3
        if num[k] > num[j]:
            j, k = k, j
        a = num[i]-num[k]
        b = num[k]-(num[j]-a)
        c = num[j]-a
        print (label[i]+label[j])*a + (label[i]+label[k])*b + (label[i]+label[j]+label[k])*c

