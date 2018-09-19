#!/usr/bin/env python

import sys
import argparse
import copy

class InputCase: # Calling this "TestCase" will make PyCharm think it's a Python unittest
    pass

def process_command_line(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=argparse.FileType('r'),
                        help="Input file")
    args = parser.parse_args()

    return args

def process_input(args):
    casescount = int(args.filename.readline())
    testcases = []

    for i in range(casescount):

        testcase = InputCase()
        # Adjust test case variables here
        casestring = args.filename.readline()
        testcase.D = int(casestring)
        secondline = args.filename.readline()
        testcase.P = map(int, secondline.split())
        testcases.append(testcase)

    args.filename.close()

    return testcases

def puzzle(t, steps):
    # print("Checking %s, with cumulative steps at %d" % (str(t.P), steps))

    tallest = max(t.P)

    if len(t.P) > max(t.P):
        # print("Width %d exceeds height %d." % (len(t.P), max(t.P)))
        return steps + tallest

    splits = []

    for i in range(1, tallest / 2 + 1):
        tcopy = copy.deepcopy(t)
        tcopy.P.pop(tcopy.P.index(tallest))
        tcopy.P.append(i)
        tcopy.P.append(tallest - i)
        splits.append(puzzle(tcopy, steps + 1))

    # print("Tried all the splits. Tallest is %d and splits are %s" % (tallest, str(splits)))
    return min(steps + tallest, min(splits)) if len(splits) > 0 else steps + tallest # the else handles t.P = [1]

def main(argv=None):
    args = process_command_line(argv)
    testcases = process_input(args)

    for t in range(len(testcases)):
        print "Case #" + str(t + 1) + ": " + str(puzzle(testcases[t], 0))

    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
