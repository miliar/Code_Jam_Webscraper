import os, sys, time, math, random
import cProfile
import operator

#DEBUG = True
DEBUG = False 

class MySolution:
    def __init__(self, inpf):
        self.inputf = open(inpf, 'r')
        self.numcases = int(self.inputf.readline())
        self.debug = DEBUG
        self.MAX_M = 25

    def init_one_case(self):
        self.distance = 0.0
        self.num_of_horses = 0
        self.horses = {}

    def load_one_case(self):
        line = self.inputf.readline().strip()
        distance_str, num_of_horses_str = line.split(' ')
        self.distance = float(int(distance_str))
        self.num_of_horses = int(num_of_horses_str)

        for i in range (self.num_of_horses):
            line1 = self.inputf.readline().strip()
            initial_position_str, max_speed_str = line1.split(' ')
            initial_position = float(int(initial_position_str))
            max_speed = float(int(max_speed_str))
            self.horses[str(i)] = [initial_position, max_speed]

    def print_error(self, name):
        print "ERROR: {0}".format(name)

    def print_output(self, case_number, annie_speed):
        print "Case #{0}: {1:.6f}".format(case_number+1, annie_speed);
  
    def get_input(self):
        self.init_one_case()
        self.load_one_case()

    def solve(self):
        for ncase in range(self.numcases):
            self.get_input()

            t = 0.0
            for i in range(self.num_of_horses):
                a_horse = self.horses[str(i)]
                d1 = a_horse[0]
                if d1 > self.distance:
                    continue
                d2 = self.distance - d1
                t1 = d2 / a_horse[1]
                a_horse = [d1 + d2 * t1, a_horse[1]]
                self.horses[str(i)] = a_horse

                if self.debug:
                    print self.horses
                    
                t = t + t1

                if i + 1 < self.num_of_horses:
                    for j in range(i+1, self.num_of_horses):
                        b_horse = self.horses[str(j)]
                        d = b_horse[0]
                        b_horse = [d + t1 * b_horse[1], b_horse[1]]
                        self.horses[str(j)] = b_horse

            self.print_output(ncase, float( self.distance) / float(t))


def print_usage():
    print "USAGE: %s <input file>".format(sys.argv[0])


if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    for one_input_file in sys.argv[1:]:
        one = MySolution(one_input_file)
        one.solve()
        #cProfile.run('one.solve()')

