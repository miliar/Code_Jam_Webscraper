#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from collections import Counter

def rev(s,j,k):
    """
    Reverse k element from the j-th in s
    """
    s[j:j+k] = ["-" if e == "+" else "+" for e in s[j:j+k]]
    return s


def main():
    """
    Do the job
    """
    t = int(sys.stdin.readline())
    for i in range(t):
        s, k = sys.stdin.readline().split()
        s = list(s)
        k = int(k)
        if s.count('-') % k != 0:
            nb_actions = "IMPOSSIBLE"
        elif "+" in s[-k:k-1] and "-" in s[-k:k-1]:
            nb_actions = "IMPOSSIBLE"
        else:
            count = 0
            while "-" in s:
                if s[j] == "-":
                    s = rev(s,j,k)
                    count += 1
                if s[-(j+1)] == "-":
                    count += 1

        print("Case #%s: %s" % (i+1, nb_actions))
    return 1

def main2():
    """
    Do the job. Better.
    """
    t = int(sys.stdin.readline())
    for i in range(t):
        s, k = sys.stdin.readline().split()
        s = list(s)
        k = int(k)
        nb_actions = 0
        for j in range(len(s)-k+1):
            if s[j] == "-":
                rev(s,j,k)
                nb_actions += 1
        if "-" in s:
            nb_actions = "IMPOSSIBLE"
        print("Case #%s: %s" % (i+1, nb_actions))
    return 1


main2()
