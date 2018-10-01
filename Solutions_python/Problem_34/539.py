#!/usr/bin/python
import re

(L, D, N) = map(int, raw_input().split())
vocabulary = []
tests = []
for i in range(D):
    vocabulary.append(raw_input())
for i in range(N):
    tests.append(raw_input().replace('(', '[').replace(')', ']'))
n_case = 1
for test in tests:
    matches = 0
    for word in vocabulary:
        if re.match(test, word):
            matches += 1
    print "Case #%d: %d" % (n_case, matches)
    n_case += 1
