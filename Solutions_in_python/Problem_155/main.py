#!/usr/bin/env python3

import logging

from sys import stdin
from sys import stdout

logger = logging.getLogger("jan")
logger.setLevel(logging.ERROR)
logger.addHandler(logging.StreamHandler(stdout))

N = int(stdin.readline().strip())

for x in range(0, N):
    line = stdin.readline().strip()
    items = line.split(" ")

    s_max = int(items[0])
    s = items[1]

    logger.debug("s_max = {}".format(s_max))
    logger.debug("s = {}".format(s))

    standing = 0
    needed = 0
    for i in range(0, s_max + 1):
        logger.debug("i = {}".format(i))
        s_i = int(s[i])
        logger.debug("s_1 = {}".format(s_i))
        if (standing < i) and (s_i > 0):
            needed += int(i - standing)
            logger.debug("needed = {}".format(needed))
            standing += needed
        standing += int(s_i)
        logger.debug("standing = {}".format(standing))

    print("Case #{}: {}".format(x + 1, needed))
    logger.debug("\n")

