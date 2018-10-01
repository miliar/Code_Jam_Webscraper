#!/usr/bin/env python

from math import sqrt

def is_fair_and_square(pal):
    s = int(sqrt(pal))
    if s*s != pal: return False
    spal = str(s)
    return spal == spal[::-1]

def gen_pals(n):
    m = 1
    i = 1
    j = None

    beg = None
    end = None
    while True:
        if m == 1:
            m = 4
            yield 1
        if m == 4:
            m = 9
            yield 4
        if m == 9:
            m = 10
            i = 1
            yield 9
        if j == None:
            if 2*len(str(i)) > n:
                break
            beg = str(i)
            end = beg[::-1]
            m = int(beg+end)
            i += 1
            if 2*len(str(i))+1 <= n:
                j = 0
            yield m
        else:
            if j != None:
                mid = str(j)
                m = int(beg+mid+end)
                j += 1
            else: m = int(beg+end)
            if (j == 10): j = None
            yield m


pals = gen_pals(13)
pals = filter(is_fair_and_square, pals)
pals = list(pals)
file = open("input.txt")
num_tests = int(file.readline().strip())
for i in range(num_tests):
    j,k = file.readline().split()
    j,k = int(j),int(k)
    tmp = pals[:]
    count = len(list(filter(lambda x: j<=x<=k, tmp)))
    print("Case #" + str(i+1) + ": " + str(count))
file.close()
