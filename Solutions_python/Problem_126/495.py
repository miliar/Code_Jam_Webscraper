#! /usr/bin/python

import os, sys
from itertools import izip

debug_flag = len(sys.argv) >= 2 and sys.argv[1] == '-d'
 
def debug(msg):
    if debug_flag:
        print msg


vowels = ['a', 'e', 'i', 'o', 'u']

T = int(raw_input())

for case in range(1, T+1):
    [name, n] = raw_input().split(' ')
    n = int(n)
    debug(name)
    debug(n)

    in_cons = False
    tot_count_cons = 0
    count_cons = 0
    max_count_cons = 0

    l = len(name)
    for i, c in enumerate(name[0:l-n+1]):
        count_cons = 0
        max_count_cons = 0
        # debug('i=%s'%i)
        # for b in name[i:i+n]:
        #     if b not in vowels:
        #         if in_cons:
        #             count_cons += 1
        #             max_count_cons = max(count_cons, max_count_cons)
        #         else:
        #             count_cons = 1
        #             max_count_cons = count_cons
        #             in_cons = True
        #     else:
        #         in_cons = False
        #     if i+n == l:
        #         if max_count_cons >= n:
        #             tot_count_cons += 1
        for j, b in enumerate(name[i:]):
            debug('found %s' % b)
            debug(name[i:i+j+1])
            if b not in vowels:
                if in_cons:
                    count_cons += 1
                    max_count_cons = max(count_cons, max_count_cons)
                else:
                    max_count_cons = max(count_cons, max_count_cons)
                    count_cons = 1
                    max_count_cons = max(count_cons, max_count_cons)
                    in_cons = True
            else:
                in_cons = False 
            debug('count_cons = %s' % max_count_cons)
            if max_count_cons >= n:
                tot_count_cons += 1
            debug('count_cons = %s' % max_count_cons)
        #debug('found vowel (2): count_cons = %s' % max_count_cons)
        #if max_count_cons >= n:
        #    tot_count_cons += 1
        
    print 'Case #%s: %s' % (case, tot_count_cons)

