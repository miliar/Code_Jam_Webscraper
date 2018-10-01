#!/usr/bin/env python

with open('C-small-1-attempt0.in') as f:
    with open('C.out', 'w') as g:
        T = int(f.readline())
        for i in xrange(T):
            N, K = [int(x) for x in f.readline().split()]
            stalls = [N]
            for j in xrange(K):
                m = max(stalls)
                s = stalls.index(m)
                #if m > 1:
                stalls[s] = (m + 1) / 2 - 1
                stalls.insert(s + 1, m - stalls[s] - 1)
                #else:
                    #stalls.pop(s)
            #print stalls
            t = []
            #print s
            g.write('Case #%d: %d %d\n' % (i+1, max(stalls[s], stalls[s+1]), min(stalls[s], stalls[s+1])))
            '''
            for j in xrange(len(stalls)):
                if j > 0 and j < len(stalls) - 1:
                    if stalls[j] > 0:
                        t.append(stalls[j])
                    else:
                        s -= 1
                else:
                    t.append(stalls[j])
            print t
            print min(t[s], t[s+1]), max(t[s], t[s+1])
            '''
