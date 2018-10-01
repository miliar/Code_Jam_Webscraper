#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

def debug(*args):
    print(*args, file=sys.stderr)

fin = sys.stdin
T = int(fin.readline())
for case in range(1, T + 1):

    N = int(fin.readline()) # 1st volunteer row
    s1 = None
    for i in range(1, 5):
        numbers = set(map(int, fin.readline().split()))
        if i == N:
            s1 = numbers


    N = int(fin.readline()) # 2nd volunteer row
    s2 = None
    for i in range(1, 5):
        numbers = set(map(int, fin.readline().split()))
        if i == N:
            s2 = numbers

    result = s1.intersection(s2)

    if len(result) > 1:
        result = "Bad magician!"
    elif len(result) < 1:
        result = "Volunteer cheated!"
    else:
        result = list(result)[0]

    print("Case #%d: %s" % (case, result))

