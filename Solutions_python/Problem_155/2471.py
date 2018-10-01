# -*- coding: utf-8 -*-

import sys


def get_required_invitations(levels):
    audience = [int(persons) for persons in levels]
    required = 0
    for level, persons in enumerate(audience):
        if not persons:
            required += 1
        if persons < 2:
            continue
        try:
            audience[level + 1] += persons - 1
        except IndexError:
            return required
        audience[level] = 1
    return required


def parse_test_file(path):
    lines = open(path).readlines()
    tests = int(lines.pop(0))
    test = 0
    while test < tests:
        test += 1
        args = lines.pop(0).split()
        print "Case #{}:".format(test), get_required_invitations(args[1])


if __name__ == "__main__":
    parse_test_file(sys.argv[1])
