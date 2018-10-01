from Solve import *
from collections import deque

def a(args):
    n = int(args[0])
    strs = args[1:]
    chars = set("".join(strs[0]))
    for i in range(1, n):
        if set("".join(strs[i])) != chars:
            return "Fegla Won"
    if n > 2:
        return "Later"

    a = strs[0]
    b = strs[1]
    len1 = len(a)
    len2 = len(b)
    lenDiff = abs(len1 - len2)
    minLen = min(len1, len2)
    diff = lenDiff

    als = toList(a, len1)
    bls = toList(b, len2)
    if len(als) != len(bls):
        return "Fegla Won"
    else:
        diff = calcDiff(als, bls)
        if diff == -1:
            return "Fegla Won"
        return diff
    return diff

def toList(s, len1):
    ls = []
    lsi = 0
    cur = s[0]
    ls.append([cur, 1])
    for i in range(1, len1):
        c = s[i]
        if c == cur:
            ls[lsi][1]+=1
        else:
            cur = c
            lsi+=1
            ls.append([c, 1])
    return ls

def calcDiff(als, bls):
    diff = 0
    lenls = len(als)
    for i in range(lenls):
        achar, acount = als[i]
        bchar, bcount = bls[i]
        if achar != bchar:
            return -1
        diff+=abs(acount-bcount)
    return diff
    
solveV("A-small-attempt1.in", a)
#solve("A-large.in", a)
