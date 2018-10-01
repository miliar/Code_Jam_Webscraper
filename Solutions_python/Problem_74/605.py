#!/usr/bin/env python
# Google Code Jam 2011
# Qualification Round
# Problem A - Bot Trust
# May 7th 2011
# David Antliff <david.antliff@gmail.com>

import sys
import itertools

class dummyStream:
    def __init__(self): pass
    def write(self,data): pass
    def read(self,data): pass
    def flush(self): pass
    def close(self): pass
# turn off stderr output
sys.stderr = dummyStream()

def signum(i):
    if (i < 0):
        return -1;
    elif (i > 0):
        return 1;
    else:
        return 0;

class Robot(object):

    MIN_LOC = 1
    MAX_LOC = 100

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.button = None
        self.push = False

    def __str__(self):
        return "%s : %d, next %d" % (self.name, self.location, self.button)

    def tick(self):
        # run a simulation tick - 1 second

        if self.push:
            # takes a tick to push the button
            self.push = False
            sys.stderr.write("%s pushed button %s\n" % (self.name, self.location))
            return

        # if a destination is programmed, move towards it
        if self.button:
            self.location += signum(self.button - self.location)
            sys.stderr.write("%s moved to %d (going to %s)\n" % (self.name, self.location, self.button))
        else:
            sys.stderr.write("%s not moving\n" % (self.name,))

    def next_button(self, button):
        sys.stderr.write("%s next button %s\n" % (self.name, button))
        self.button = button

    def push_button(self):
        self.push = True


import itertools

class TestCase(object):

    def __init__(self, program_string):
        tokens = program_string.split()
        num = int(tokens.pop(0))
        assert(2 * num == len(tokens))
        self.program = list(itertools.izip_longest(*[iter(tokens)]*2))

    def __str__(self):
        return "%s" % (list(self.program),)

    def lookahead(self, this_robot):
        for robot, button in self.program:
            if this_robot == robot:
                return int(button)
        return None

    def run_test(self):
        sys.stderr.write(str(self) + "\n")

        ticks = 0

        robots = dict()
        robots['O'] = Robot("Orange", 1)
        robots['B'] = Robot("Blue", 1)

        # set initial instructions
        robots['O'].next_button(self.lookahead('O'))
        robots['B'].next_button(self.lookahead('B'))

        robot, button = self.program.pop(0)
        button = int(button)

        # send instructions to robots, and run the main loop
        while 1:

            ticks += 1
            sys.stderr.write("tick %d\n" % (ticks,))

            if robots[robot].location == button:
                robots[robot].push_button()
                robots[robot].next_button(self.lookahead(robot))

                if self.program:
                    robot, button = self.program.pop(0)
                    button = int(button)
                else:
                    # program finished
                    sys.stderr.write("program finished at %d\n" % (ticks,))
                    break

            robots['O'].tick()
            robots['B'].tick()


        return ticks


def main():

    #input = sys.stdin
    input = open(sys.argv[1], 'r')

    test_cases = []

    # read input file
    T = int(input.readline())  # number of cases

    for i in range(T):
        line = input.readline()
        test_cases.append( TestCase(line) )

    assert(len(test_cases) == T)

    # process test cases
    R = process_test_cases(test_cases)
    assert(len(R) == T)

    # print output file
    for i, r in enumerate(R):
        print("Case #%d: %s" % (i + 1, r))


def process_test_cases(test_cases):

    results = []
    num = len(test_cases)

    for i, case in enumerate(test_cases):
        sys.stderr.write("test case %d / %d\n" % (i + 1, num))
        r = case.run_test()
        results.append(r)

    return results



if __name__ == "__main__":
    main()
