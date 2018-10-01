#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import sys

no = 'Impossible'

def mk_grid(r, c, m):
    # note: this code is a mess, don't have time to refactor
    _m = m

    # easy cases

    if r == 1 and c == 1:
        return 'c'

    if r == 1:
        return 'c' + ('*' * m).rjust(c-1, '.')

    if c == 1:
        l = 'c' + ('*' * m).rjust(r-1, '.')
        return '\n'.join(list(l))

    if r*c - m == 1:
        return 'c' + '*' * (c-1) + '\n' + '\n'.join(['*'*c]*(r-1))

    # /

    rev = False

    #if c < r:
    if m%r == 0:
        r, c = c, r
        rev = True

    g = [['.'] * c for _ in range(r)]

    fr = fc = 0 # filed row, columns
    cc = c
    rr = r

    while True:
        d=False
        if fr < r-2 and m >= cc:
            d=True
            g[fr] = ['*'] * c
            fr += 1
            rr -= 1
            m -= cc

        if fc < c-2 and m >= rr:
            d=True
            for l in g:
                l[fc] = '*'

            fc += 1
            cc -= 1
            m -= rr

        if not d:
            break

    if m > 0:
        ok = False
        for xc in range(fc, c-2):
            if ok:
                break
            for xr in range(fr, r-2):
                g[xr][xc] = '*'
                m -= 1
                if m == 0:
                    ok = True
                    break

    g[-1][-1] = 'c'

    if m > 0:
        return no

    if rev:
        g = [[l[i] for l in g] for i in xrange(len(g[0]))]

    return '\n'.join([''.join(r) for r in g])


def next_turn(f):
    R, C, M = map(int, f.readline().replace('\n', '').split(' '))

    rc    = R*C
    empty = rc - M
    poss = False

    poss = (empty >= 4) or (empty == 1) or ((R == 1 or C == 1) and empty >= 1)

    if not poss:
        return no

    g = mk_grid(R, C, M)
    return g


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "usage: %s <input file>" % sys.argv[0]
        sys.exit(1)

    with open(sys.argv[1]) as f:
        with open("%s.out" % sys.argv[1], 'w') as out:
            c = int(f.readline())
            for i in range(1, c+1):
                out.write('Case #%d:\n%s\n' % (i, next_turn(f)))
    print 'done.'

