#! /usr/bin/env python

# usage: python template.py <file.in >file.out

# fuck subset sum

T = int(raw_input())
for case in xrange(1, T+1):
    line = map(int, raw_input().split(' '))
    N, S = line[0], line[1:]
    subset_sums = []
    found, found2 = False, False
    for x in xrange(1, 2**N):
        subset_sum = 0
        for i in xrange(20):
            if x & 2**i:
                subset_sum += S[i]
        if subset_sum in subset_sums:
            found, found2 = x, subset_sums.index(subset_sum) + 1
            break
        subset_sums.append(subset_sum)
    string, string2 = [], []
    if found:
        for i in xrange(20):
            if found & 2**i:
                string.append(str(S[i]))
        for i in xrange(20):
            if found2 & 2**i:
                string2.append(str(S[i]))
    print "Case #%s:\n%s\n%s" %(case, ' '.join(string), ' '.join(string2))
