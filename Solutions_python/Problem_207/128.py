#!/usr/bin/env python

import sys
import logging

log = logging.getLogger(__name__)
logging.basicConfig()


class Impossible(Exception):
    pass


def print_result(result, i):
    sys.stdout.write("Case #%s: %s\n" % (i, result))


def readline():
    return sys.stdin.readline().rstrip('\n')


def splitline(f=str):
    return map(f, readline().split())


def position(MAX, MED, MIN):
    if len(MAX) > len(MED) + len(MIN):
        raise Impossible

    res = ""
    while len(MAX) > len(MED):
        res += MAX.pop()
        res += MED.pop()
        res += MAX.pop()
        res += MIN.pop()

    while MIN:
        res += MAX.pop()
        res += MED.pop()
        res += MIN.pop()

    while MAX:
        res += MAX.pop()
        res += MED.pop()

    return res


def solve():
    N, R, O, Y, G, B, V = splitline(int)
    blocks = {"R": ["R"] * R,
              "Y": ["Y"] * Y,
              "B": ["B"] * B}

    if G:
        if G > R:
            raise Impossible
        if G == R:
            if any((O, Y, B, V)):
                raise Impossible
            return "GR" * G
        blocks["R"] = blocks["R"][G:]
        blocks["R"][0] = "R" + "GR" * G
        R -= G
    if V:
        if V > Y:
            raise Impossible
        if V == Y:
            if any((R, O, G, B)):
                raise Impossible
            return "VY" * V
        blocks["Y"] = blocks["Y"][V:]
        blocks["Y"][0] = "Y" + "VY" * V
        Y -= V
    if O:
        if O > B:
            raise Impossible
        if O == B:
            if any((R, Y, G, V)):
                raise Impossible
            return "OB" * O
        blocks["B"] = blocks["B"][O:]
        blocks["B"][0] = "B" + "OB" * O
        B -= O

    if max(R, Y, B) == R:
        if Y > B:
            return position(blocks["R"], blocks["Y"], blocks["B"])
        else:
            return position(blocks["R"], blocks["B"], blocks["Y"])
    elif max(R, Y, B) == Y:
        if R > B:
            return position(blocks["Y"], blocks["R"], blocks["B"])
        else:
            return position(blocks["Y"], blocks["B"], blocks["R"])
    elif max(R, Y, B) == B:
        if R > Y:
            return position(blocks["B"], blocks["R"], blocks["Y"])
        else:
            return position(blocks["B"], blocks["Y"], blocks["R"])


def main():
    for i in xrange(int(readline())):
        try:
            res = solve()
        except Impossible:
            res = "IMPOSSIBLE"
        print_result(res, i + 1)


if __name__ == '__main__':
    main()
