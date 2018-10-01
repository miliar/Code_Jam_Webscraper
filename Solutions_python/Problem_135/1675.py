#!/usr/bin/env python
T = input()
for t in xrange(T):
    x = input()
    A = []
    for i in xrange(4):
        A.append(map(int, raw_input().split()))
    y = input()
    B = []
    for i in xrange(4):
        B.append(map(int, raw_input().split()))
    z = set(A[x-1]) & set(B[y-1])
    if len(z) == 1:
        print 'Case #%d: %d' % (t+1, list(z)[0])
    elif len(z) == 0:
        print 'Case #%d: %s' % (t+1, 'Volunteer cheated!')
    else:
        print 'Case #%d: %s' % (t+1, 'Bad magician!')
