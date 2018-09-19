""" Welcome to Code Jam

:Abstract: Solution to Google Code Jam 2011 qualification
:Authors:  iki
:Contact:  jan.killian at (g)mail.com

.. contents::

Problem statement
=================

Input
-----

Output
------

Limits
------

Doctest
=======

>>> test(
...   testlabel='sample via parse()',
...   testinput='''2
... 2 20 8 2 3 5
... 1 4 2 2 10 4
... ''')  #doctest: +NORMALIZE_WHITESPACE
Case #1: 54
Case #2: 20
"""
__docformat__ = 'restructuredtext en'

from codejam import *

def s(seq):
    return ''.join(map(chr, seq)) or '-'

def solve(L, t, N, C, D):
    if log.debug: log.debug('L %d, t %d, N %d, C %d = %d' % (L, t, N, C, len(D)))
    assert C == len(D)
    if log.debug: log.debug(D)

    CK, CJ = divmod(N, C)
    CD = sum(D)
    TD = CK * CD + sum(D[:CJ])
    TT = TD * 2
    if log.debug: log.debug('CK %d * C %d + CJ %d = N %d' % (CK, C, CJ, N))
    if log.debug: log.debug('CK %d * CD %d + sum(D[:CJ %d]) %d = TD %d' % (CK, CD, CJ, sum(D[:CJ]), TD))
    if not L:
        return TT

    T2 = t / 2.0
    AK, AD = divmod(T2, CD)
    AJ = 0
    ad = 0
    for d in D:
        AJ += 1
        ad += d
        if ad >= AD:
            AL = ad - AD
            break
    if log.debug: log.debug('AK %d * CD %d + AD %d (= sum(D[:AJ %d] %d - AL %d) = t / 2 %d' % (AK, CD, AD, AJ, sum(D[:AJ]), AL, T2))

    SD = {}
    if AK < CK:
        if AK < CK - 1:
            x = CK - AK
            for d in D:
                SD[d] = SD.get(d, 0) + x
        for d in D[AJ:]:
            SD[d] = SD.get(d, 0) + 1
        if AL:
            SD[AL] = SD.get(AL, 0) + 1
        for d in D[:CJ]:
            SD[d] = SD.get(d, 0) + 1
    elif AK == CK:
        for d in D[AJ:CJ]:
            SD[d] = SD.get(d, 0) + 1
        if AL and AJ <= CJ:
            SD[AL] = SD.get(AL, 0) + 1
    else:
        return TT

    if log.debug: log.debug(SD)

    for d in reversed(sorted(SD.keys())):
        x = min(SD[d], L)
        L -= x
        TT -= x * d
        if log.debug: log.debug('TT %d - %d * %d = %d, L %d - %d = %d' % (TT + x*d, x, d, TT, L+x, x, L))
        if not L:
            break
    return int(TT)

def parse(fi):
    D = map(int, fi.next().split())
    return D[0], D[1], D[2], D[3], D[4:]

def format(r):
    return r

if __name__ == '__main__':
    main(solve, parse, format)
