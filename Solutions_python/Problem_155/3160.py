#!/usr/bin/env python
import pdb

#pdb.set_trace()
T = input()

for t in xrange(0, T):
    S = map(int, raw_input().split()[1])
    friends = 0
    
    standing = 0
    for i in xrange(0, len(S)):
        if S[i] == 0:
            continue
        complement = i - standing
        if complement > 0:
            friends = friends + complement
            standing = standing + complement

        standing = standing + S[i]


    print 'Case #%d: %d' % (t+1, friends)
