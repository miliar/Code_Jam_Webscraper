#!/usr/bin/env python

import sys

lines = [x.strip() for x in sys.stdin.readlines()]

lines = lines[1:]
results = []

k = False
for l in lines :
    if not k :
        N,L,H = [int(x) for x in l.split()]
        k = True
        continue
    k = False
    passed = False
    nums = [int(x) for x in l.split()]
    i = L
    while i < H + 1 :
        passed = True
        for n in nums :
            if i % n != 0 and n % i != 0 :
                passed = False
                break
        if passed :
            results.append(i)
            break
        i += 1
    if not passed :
        results.append("NO")

for i in xrange(len(results)): 
    print "Case #" + str(i+1) + ": " + str(results[i])
