#!/usr/bin/env python

import sys
import logging
import argparse


def solve(A):
    tmp = [(a, i) for (i, a) in enumerate(A)]
    tmp.sort()
    B = [-1] * len(A)
    for idx, t in enumerate(tmp):
        B[t[1]] = idx
    logging.debug("A: %s", A)
    logging.debug("B: %s", B)

    N = len(A)
    total = 0

    for i in xrange(N):
        left = 0
        right = 0
        is_left = True
        for x in B:
            if x == i:
                is_left = False
            elif x > i:
                if is_left:
                    left += 1
                else:
                    right += 1
        total += min(left, right)

    return total

def main(inp, output):
    T = int(next(inp))
    for case in range(1,T+1):
        N = int(next(inp))
        A = [int(x) for x in next(inp).split()]
        r = solve(A)
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
