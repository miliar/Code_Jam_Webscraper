#!/usr/bin/env python

import sys
from bisect import bisect

def war(n_blocks, k_blocks):
    k_blocks = k_blocks[:]
    n_score = 0
    for nb in n_blocks:
        try:
            kb = k_blocks.pop(bisect(k_blocks, nb))
        except IndexError:
            kb = k_blocks.pop(0)
        n_score += nb > kb
    return n_score

def main(in_stream, out_stream):
    n_cases = int(in_stream.next())
    for i in xrange(1, n_cases+1):
        N = int(in_stream.next())
        n_blocks = sorted(map(float, in_stream.next().split()))
        k_blocks = sorted(map(float, in_stream.next().split()))
        assert len(n_blocks) == len(k_blocks) == N
        w_score = war(n_blocks, k_blocks)
        dw_score = N - war(k_blocks, n_blocks)
        out_stream.write('Case #%d: %d %d\n' % (i, dw_score, w_score))

if __name__ == '__main__':
    main(sys.stdin, sys.stdout)
