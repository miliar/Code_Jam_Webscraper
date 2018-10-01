#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from sys import stderr
from collections import deque, defaultdict
from itertools import *

def mainSmall():
    data = deque(map(int,sys.stdin.read().split()))
    token = data.popleft
    T = int(token())

    palsq = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001,
             1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521,
             400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321,
             40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201,
             1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321,
             1234567654321,
             4000008000004, 4004009004004, 100000020000001, 100220141022001,
             102012040210201,
             102234363432201, 121000242000121, 121242363242121,
             123212464212321, 123456787654321]

    def test():
        l = token()
        h = token()
        return len([x for x in palsq if l <= x <= h])



    for case in xrange(1, T+1):
        print "Case #%d: %s" % (case, test())
        sys.stdout.flush()

mainSmall()

def is_pal(x):
    return str(x)[::-1] == str(x)

def is_sq_pal_base(x):
    return is_pal(x) and is_pal(x*x)

#print [x*x for x in xrange(1,20000000) if is_sq_pal_base(x)]
