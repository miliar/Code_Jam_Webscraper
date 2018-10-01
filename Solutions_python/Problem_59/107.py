#!/usr/bin/env python

import logging

INPUT_FILENAME = "A-small-attempt0.in"
INPUT_FILENAME = "A-large.in"


def main():
    input = file(INPUT_FILENAME)
    num_cases = int(input.readline().rstrip())
    for case in xrange(1, num_cases + 1):
        N, M = [int(v) for v in input.readline().rstrip().split()]
        existing = set()
        for i in xrange(N):
            existing.add(input.readline().rstrip())
        existing.add("/")
        existing.add("")

        mkdirs = 0
        for i in xrange(M):
            path = input.readline().rstrip()
            while path not in existing:
                mkdirs += 1
                existing.add(path)
                path = path.rsplit("/", 1)[0]

        print "Case #%s: %s" % (case, mkdirs)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    try:
        import psyco
        psyco.full()
    except ImportError:
        logging.warn("No psyco speedup")
    main()

