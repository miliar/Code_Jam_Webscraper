#!/usr/bin/python3

import re
#import matplotlib.pyplot as plt
import sys
import itertools
import math
import logging
from functools import partial
import argparse

# CodeJam I/O helpers adapted from royf

# A single word (minus whitespace)
def read_word(f):
    return next(f).strip()

# A single int (given base)
def read_int(f, base=10):
    return int(read_word(f), base)

# A list of characters (including whitespace)
def read_letters(f):
    return list(read_word(f))

# A list of digits (whitespace results in error)
def read_digits(f, base=10):
    return [int(x, base) for x in read_letters(f)]

# A list of words split by whitespace
def read_words(f, delimiter=' '):
    return read_word(f).split(delimiter)

# A list of values interpreted by converter, split by delimiter
def read_values(f, converter, delimiter=' '):
    return [converter(x) for x in read_words(f, delimiter)]

# A list of ints split by whitespace
def read_ints(f, base=10, delimiter=' '):
    return read_values(f, partial(int,base=base), delimiter)

# Read 'length' lines, return a list interpreting each line using 'reader=read_ints'
# Use functools.partial to specify reader arguments
def read_arr(f, length, reader=read_ints):
    res = []
    for _i in range(length):
        res.append(reader(f))
    return res

def solve(in_file, out_fn=None):
    if out_fn is None:
        out_fn = re.match('(.+)\.in',in_file.name).groups()[0] + '.out'
    with open(out_fn, 'w') as fo:
        setup()
        T = read_int(in_file)
        for case_num in range(1, T+1):
            case = read_case(in_file)
            answer = solver(case)
            logging.info("Solved case {}".format(case_num))
            write_case(fo, case_num, answer)

################################################################################

def read_case(f):
    maxshyness,shyness = read_words(f)
    return [int(c) for c in shyness]

def write_case(f, case_num, answer):
    output = "Case #{}: {}\n".format(case_num, answer) 
    logging.debug(output)
    f.write(output)

################################################################################

def write_tests(outfilename, size, numcases=None):
    import random

    small = size == 'small'

    if numcases == None:
        if small:
            numcases = 100
        else:
            numcases = 100

    cases = []
    for tnum in range(numcases):
        if small:
            numflies = random.randint(3,10)
        else:
            numflies = random.randint(3,500)

        case = "{}\n".format(numflies)
        for fnum in range(numflies):
            case += " ".join(map(str,random.sample(range(-5000,5000),6))) + "\n"

        cases.append(case)

    with open(outfilename,'w') as outfile:
        outfile.write("{}\n".format(numcases))
        for case in cases:
            outfile.write(case)
        outfile.close()

################################################################################

def solver(case):
    logging.debug(case)
    up = 0
    friends = 0
    for level,people in enumerate(case):
        if people > 0:
            if up >= level:
                up += people
            else:
                # These people won't stand up without help.
                diff = level - up
                friends += diff
                up += diff
                up += people
                logging.debug("Shyness {}, {} people, {} new friends".format(level, people, diff))

    return friends


# Globals
def setup():
    return

################################################################################

parser = argparse.ArgumentParser()
parser.add_argument('testfile', nargs='?', type=argparse.FileType('r'), help='Name of file to solve (must end with ".in")')
parser.add_argument( '--tests',  nargs='?', const="tests.in", help='Write tests instead of solving them')
parser.add_argument('--testsize', choices=["small","large"], metavar="SIZE", default="small", help="whether to make large or small tests")
parser.add_argument('--testcases', type=int, metavar="N", help="Number of test cases to produce")
args = parser.parse_args()

logging.basicConfig(format="%(message)s", level=logging.DEBUG)
if args.tests:
    write_tests(args.tests, args.testsize, args.testcases)
else:
    if args.testfile:
        solve(args.testfile)
    else:
        parser.error("You must specify an input filename if not using --tests")
