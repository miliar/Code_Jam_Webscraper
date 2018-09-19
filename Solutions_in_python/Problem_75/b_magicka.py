#!/usr/bin/env python

from collections import defaultdict

base = 'QWERASDF'

T = input()
for t in xrange(1,T+1):
    line = raw_input()
    line = line.split()
    i = 0;
    C = int(line[i])
    combs = dict()
    for c in range(C):
        comb = line[1+c]
        combs[''.join(sorted(comb[:-1]))] = comb[-1]

    D = int(line[C+1])

    oppsd = defaultdict(set)
    for d in range(D):
        opp = line[C+2+d]
        a,b = opp
        oppsd[a].add(b)
        oppsd[b].add(a)

    s = line[C+D+3]
    l = []
    for c in s:
        l.append(c)
        if len(l) > 1:
            # check for combination
            if l[-2] in base:
                m = ''.join(sorted(l[-2:]))
                if m in combs:
                    l[-2:] = combs[m]
                    continue    #can't combine more than once
            #check for opposition
            if l[-1] in oppsd:
                for i in xrange(len(l)-1):
                    if l[i] in oppsd[l[-1]]:
                        l = []
                        break
    print "Case #%d: [%s]"%(t,', '.join(l))
