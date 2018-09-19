#!/usr/bin/env python

import sys
import logging
import argparse
import itertools

def count_up(words):
    count = 1
    prev = ""
    for w in words:
        for j in xrange(len(w)):
            if j >= len(prev) or w[j] != prev[j]:
                count += len(w) - j
                break
        prev = w
    logging.debug('words: %s words, score: %s', words, count)
    return count


def solve(N, S):
    worst = 1
    count = 0
    S.sort()
    M = len(S)

    for xs in itertools.product(range(N), repeat=M):
        ts = [list() for x in xrange(N)]
        for i, x in enumerate(xs):
            ts[x].append(S[i])
        if not all(ts):
            continue

        c = 0
        for t in ts:
            c += count_up(t)
        if c > worst:
            worst = c
            count = 0
        if c == worst:
            count += 1
            count = count % 1000000007
    return "%s %s" % (worst, count)

def main(inp, output):
    T = int(next(inp))
    for case in range(1,T+1):
        M, N = [int(x) for x in next(inp).split()]
        S = []
        for m in xrange(M):
            S.append(next(inp).strip())
        r = solve(N, S)
        s = "Case #%d: %s" % (case, r)
        print(s)
        output.write(s + "\n")
        logging.info(s)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="run code jam problem")
    parser.add_argument("filename", type=str, help="input filename")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="enable verbose logging")

    args = parser.parse_args()
    if args.verbose:
        level=logging.DEBUG
    else:
        level=logging.INFO
    logging.basicConfig(level=level,
                        filename="logfile.txt",
                        filemode="w")
    outfile = args.filename + ".out"

    with open(args.filename) as inp:
        with open(outfile, "w") as outp:
            main(inp, outp)
