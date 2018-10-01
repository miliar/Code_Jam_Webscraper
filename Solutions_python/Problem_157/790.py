#!/usr/local/bin/python

import sys
import math

table ={ ("1" , "1") : ("1",  1),
         ("1",  "i") : ("i",  1),
         ("1",  "j") : ("j",  1),
         ("1",  "k") : ("k",  1),
         ("i",  "1") : ("i",  1),
         ("i",  "i") : ("1", -1),
         ("i",  "j") : ("k",  1),
         ("i",  "k") : ("j", -1),
         ("j",  "1") : ("j",  1),
         ("j",  "i") : ("k", -1),
         ("j",  "j") : ("1", -1),
         ("j",  "k") : ("i",  1),
         ("k",  "1") : ("k",  1),
         ("k",  "i") : ("j",  1),
         ("k",  "j") : ("i", -1),
         ("k",  "k") : ("1", -1), }


def mult(a, b):
    (t1, s1) = a
    (t2, s2) = b
    
    (t, s) = table[(t1, t2)]
    s = s * s1 * s2
    return (t, s)

T = int(sys.stdin.readline())

for caseno in xrange(T):
    L, X = [int(x) for x in sys.stdin.readline().split()]
    instr = sys.stdin.readline().strip()

    one = ("1", 1)
    iterm = ("i", 1)
    jterm = ("j", 1)
    kterm = ("k", 1)

    first  = one
    second = one
    third  = one 
    ans = None

    last_ones = [one] * (L * X)
    for r in xrange(L * X):
        curr = (instr[(L * X - r - 1) % L], 1)
        if r == 0:
            last_ones[-(r+1)] = curr 
        else :
            last_ones[-(r +1)] = mult(curr, last_ones[-r])

    for i in xrange(L * X  - 2):

        if ans:
            break

        first = mult(first, (instr[i%L], 1))

        if first != iterm:
            continue

        second = None
        for j in xrange(i + 1, L * X - 1):
            if second is None:
                second = (instr[j%L], 1)
            else:
                second = mult(second, (instr[j%L], 1))

            if second != jterm:
                continue

            third = last_ones[j+1]

            if third == kterm:
                ans = "YES"
                break

    if ans is None:
        ans = "NO"

    print "Case #%d: %s" % (caseno + 1, ans)


