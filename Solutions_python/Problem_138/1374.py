#!/usr/bin/env python

def war(n,k):
    cnt = 0
    while len(n) > 0:
        if n[-1] > k[-1]:
            cnt += 1
            del k[0]
        else:
            del k[-1]
        del n[-1]
    return cnt

def decwar(n,k):
    cnt = 0
    while len(n) > 0:
        mink = min(k)
        minnidx = -1
        for i, e in enumerate(n):
            if e > mink:
                minnidx = i
                break
        if minnidx >= 0:
            cnt += 1
            del k[0]
            del n[minnidx]
        else:
            del k[-1]
            del n[-1]
    return cnt

if __name__ == '__main__':
    t = int(raw_input())
    for tc in range(1,t+1):
        items_n = int(raw_input())
        n = map(float,raw_input().split())
        k = map(float,raw_input().split())
        n = sorted(n)
        k = sorted(k)
        print "Case #%d: %d %d" % (tc, decwar(n[:],k[:]), war(n,k))
