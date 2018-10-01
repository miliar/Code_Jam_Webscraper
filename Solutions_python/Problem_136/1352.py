#!/usr/bin/env python

"""
Google Code Jam 2014
Qualification round
Problem B. Cookie Clicker Alpha

Approach:
First, a premise: If you're going to buy a farm, you always want to buy it as early as possible
(when you have 500 cookies), because you will always wind up with more cookies at any future time
T having bought at exactly 500 than if you'd waited for any period after hitting 500.

With that premise down:
Basically the graph of cookies vs. time is a sawtooth curve, and the angle of the tooth gets a little steeper
every time you buy a farm. At any given time, you're comparing two values of time T:
-The value of T when you cross X if you do buy a farm the last time you hit 500 cookies
-The value of T when you cross X if you do not buy a farm the last time you hit 500 cookies

So, for example, in the problem sample, first you're comparing
Don't buy a farm - T = (2000 / 2) = 1000
Do buy a farm - T = (500 / 2) + (2000 / 6) = 583.3333333

Between those two, you'd rather take "do buy a farm." Then, if you do the math for the next farm purchase,
T = (500 / 2) + (500 / 6) + (2000 / 10) = 533.333333

you can see that's a little faster still. But it won't always get faster.
The question is when does this series of calculations hit its minimum.
So you want to return the first T(i) such that T(i-1) > T(i) < T(i+1). You don't need to keep the
whole history of T's in memory, only the three most recent.

In the example:
T(1) = (500 / 2) = 1000
T(2) = (500 / 2) + (2000 / 6) = 583.333...
T(3) = (500 / 2) + (500 / 6) + (2000 / 10) = 533.333...
T(4) = (500 / 2) + (500 / 6) + (500 / 10) + (2000 / 14) = 526.19047613
T(5) = (500 / 2) + (500 / 6) + (500 / 10) + (500 / 14) + (2000 / 16) = 544.04761904

Which is when you see T(3) > T(4) < T(5), so you return T(4).


"""

import sys
import argparse

class TestCase:
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
        casestring = args.filename.readline()

        testcase = TestCase()
        testcase.C, testcase.F, testcase.X = map(float, casestring.split())
        testcases.append(testcase)

    args.filename.close()

    return testcases

def puzzle(t):
    Tthisterm = (t.X / 2.0)

    # first farm
    T1termago = Tthisterm
    Tthisterm = (t.C / 2) + (t.X / (2 + t.F))
    basis = (t.C / 2)

    # comparison must be <= instead of <, in case the minimum of the cookies v. time curve rests between
    # two discrete farm buildings
    if T1termago <= Tthisterm:
        return '%(T)#.7f' % {"T": T1termago}

    # second farm
    T2termsago = T1termago
    T1termago = Tthisterm
    Tthisterm = (t.C / 2) + (t.C / (2 + t.F)) + (t.X / (2 + (2*t.F)))
    basis = basis + (t.C / (2 + t.F))

    if T2termsago > T1termago and T1termago <= Tthisterm:
        return '%(T)#.7f' % {"T": T1termago}

    # third farm, written out to clearly see the iteration
    T2termsago = T1termago
    T1termago = Tthisterm
    Tthisterm = (t.C / 2) + (t.C / (2 + t.F)) + (t.C / (2 + (2 * t.F))) + (t.X / (2 + (3*t.F)))
    basis = basis + (t.C / (2 + (2 * t.F)))

    if T2termsago > T1termago and T1termago <= Tthisterm:
        return '%(T)#.7f' % {"T": T1termago}

    # fourth farm and on
    farms = 4
    while not (T2termsago > T1termago and T1termago <= Tthisterm):
        T2termsago = T1termago
        T1termago = Tthisterm
        Tthisterm = basis + (t.C / (2 + ((farms - 1) * t.F))) + (t.X / (2 + (farms * t.F)))
        # debug print "Farms: " + str(farms) + " This term: " + str(Tthisterm)

        basis = basis + (t.C / (2 + ((farms - 1) * t.F)))
        farms += 1

    return '%(T)#.7f' % {"T": T1termago}

def main(argv=None):
    args = process_command_line(argv)
    testcases = process_input(args)

    for t in range(len(testcases)):
        print "Case #" + str(t + 1) + ": " + str(puzzle(testcases[t]))

    return 0

if __name__ == '__main__':
    status = main()
    sys.exit(status)
