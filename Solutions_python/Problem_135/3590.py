#!/usr/bin/env python3

import sys
import argparse


def parse_args():
    """
    Handle command-line arguments.
    """
    parser = argparse.ArgumentParser(description=__doc__,
                                     fromfile_prefix_chars='@')
    parser.add_argument('infile',
                        type=argparse.FileType('r'), nargs='?',
                        default=sys.stdin, help='input file')
    parser.add_argument('outfile',
                        type=argparse.FileType('w'), nargs='?',
                        default=sys.stdout, help='output file')
    return parser.parse_args()


def next_int(case):
    return int(next(case).rstrip())


def split_line(line):
    return line.rstrip().split(' ')


def get_line(case):
    a = next_int(case)
    for row in range(4):
        line = next(case).rstrip()
        if a == row + 1:
            target = set(split_line(line))
    return target


def solve(case):
    a = get_line(case)
    b = get_line(case)
    intersect = a & b
    l = len(intersect)
    if l == 1:
        return intersect.pop()
    elif l > 1:
        return "Bad magician!"
    elif l < 1:
        return "Volunteer cheated!"
    else:
        raise Exception("Should not get here.")


def main():
    args = parse_args()

    with args.infile as infile, args.outfile as outfile:
        n = next_int(infile)

        for c in range(n):
            s = solve(infile)
            outstr = "Case #{:d}: {:s}".format(c + 1, s)
            print(outstr, file=outfile)


if __name__ == '__main__':
    exit = main()
    if exit:
        sys.exit(exit)
