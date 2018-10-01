#!/usr/bin/env python

import sys
import logging

if len(sys.argv) == 2 and sys.argv[1] == '-v':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(message)s')
else:
    logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')


def split(n):
    if n == 2:
        return [0, 1]
    if n == 1:
        return [0, 0]
    half = (n - 1) / 2
    L = half
    R = n - 1 - half
    return (L, R)


def strategy(N, K):
    logging.debug("  < N={}, K={}".format(N, K))

    count = 0
    S = [N]
    while count < K:
        newS = []
        for s in S:
            count += 1
            logging.debug(S)
            (l, r) = split(s)
            if count == K:
                logging.debug("  The k-th is on #%d [L:%s]" % (count, l))
                return "{} {}".format(r, l)
            newS.append(l)
            newS.append(r)
        S = sorted(newS, reverse=True)

    (min, max) = (0, 0)
    return "%s %s" % (max, min)


def main(infile):
    n = int(infile.readline())
    for i in range(n):
        line = infile.readline().split()
        N = int(line[0])
        K = int(line[1])
        logging.debug("Starting case #%s" % (i + 1))
        logging.info('Case #%s: %s' % (i + 1, strategy(N, K)))

main(sys.stdin)
