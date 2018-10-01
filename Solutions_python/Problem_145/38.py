""" imports """
#pylint: disable=W0622
#pylint: disable=E0102
from __future__ import division
import glob, pickle, os, time, sys, argparse
from copy import copy
from numpy import array, sin, cos
import numpy as np
from pylab import *
from fractions import gcd
from pprint import pprint
#pylint: disable=W0621


""" global variables """

""" classes """

""" functions """
powers_of_2 = [2**x for x in arange(0, 41)]
def is_power_of_2(q):
    return q in powers_of_2

def toint(i):
    assert int(i) == i
    return int(i)

def solve(P, Q):
    common_denom = gcd(P, Q)
    P, Q = [x/common_denom for x in (P, Q)]
    while Q < 2**40:
        P, Q = [x*2 for x in (P, Q)]
        if is_power_of_2(Q):
            break
    else:
        return "impossible"
    return toint(log2(Q)) - toint(floor(log2(P)))


""" parse input """
## parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("filename", default="default.in", nargs='?')
parser.add_argument("-t", "--test", action="store_true")
parser.add_argument("-l", "--lazytest", action="store_true")
args = parser.parse_args()
output = ""
TIC = time.time()

## read input lines
input_lines = open(args.filename).readlines()
def read_line():
    return input_lines.pop(0).strip()
def read_ints():
    return [int(x) for x in read_line().split(' ')]
def read_floats():
    return [float(x) for x in read_line().split(' ')]
(numquestions,) = read_ints()
for questionindex in xrange(numquestions):
    ### parse input ###
    P, Q = [int(xx) for xx in read_line().split('/')]

    ### calculate answer ###
    answer = solve(P, Q)
    assert answer != None

    ### output ###
    #print "Calculating case #{}...".format(questionindex+1)
    answer_str = "Case #{}: {}".format(questionindex+1, answer)
    output += answer_str + '\n'
    print answer_str

## write output
ofile = open('output', 'w').write(output)
TOC = time.time()
#print "done in {} s".format(TOC-TIC)


""" test """
if args.test:
    def filter_extension(filename):
        filename_parts = filename.split('.')
        if len(filename_parts) > 1:
            filename_parts = filename_parts[:-1]
        return '.'.join(filename_parts)

    print
    print "== TESTING VALIDITY =="

    try:
        # check if all input was used
        assert not len([l for l in input_lines if l.strip()]), "Not all input was used"

        # filter extension of filename
        filename_without_extension = filter_extension(args.filename)

        # get calculated and correct lines
        calculated_lines = [l.strip() for l in output.split('\n') if l.strip()]
        correct_lines = [l.strip() for l in open("{}.out".format(filename_without_extension)).readlines() if l.strip()]

        # check if number of lines match
        assert len(correct_lines) == len(calculated_lines), "calculated {} lines but expected {}".format(len(calculated_lines), \
                                                            len(correct_lines))

        # apply lazytest: filter away test numer
        unfiltered_calculated_lines = calculated_lines
        unfiltered_correct_lines = correct_lines
        if args.lazytest:
            def filter_test_number(line):
                if line.startswith("Case #"):
                    parts = line.split('#')
                    parts[1] = parts[1][parts[1].index(':'):]
                    return '#'.join(parts)
                else:
                    return line
            calculated_lines = [filter_test_number(l) for l in calculated_lines]
            correct_lines = [filter_test_number(l) for l in correct_lines]

        # get lines that don't match
        incorrect_line_numbers = []
        for line_number, (correct_line, calculated_line) in enumerate(zip(correct_lines, calculated_lines)):
            if correct_line != calculated_line:
                incorrect_line_numbers.append(line_number)
        if len(incorrect_line_numbers):
            error_msg = "\n"
            for line_number in incorrect_line_numbers:
                error_msg += '    "{}"  should be  "{}"\n'.format(unfiltered_calculated_lines[line_number],
                                                                  unfiltered_correct_lines[line_number])
            raise AssertionError(error_msg)

        print "SUCCESS"

    except AssertionError as ex:
        print "\nFAILED:"
        print str(ex)
    print
