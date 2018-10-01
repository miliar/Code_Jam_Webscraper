#!/usr/bin/python
#
# ./template.py -i template.inpt 
#

import math
from optparse import OptionParser
from operator import itemgetter, attrgetter, methodcaller

def parse_input(input_fname):
    input_arr = []
    f = open(input_fname, "r")

    # READ TESTCASE NUMBER
    testcase_num = int(f.readline())

    for t in range(0, testcase_num):
        line1       = f.readline().rstrip('\n').split()
        line2       = f.readline().rstrip('\n').split()
        line2_int   = map(lambda x: int(x), line2)
        input_arr.append([int(line1[0]), int(line1[1]), line2_int])

    return input_arr

def write_output(output_fname, output_arr):
    f = open(output_fname, "w")
    for i in range(0, len(output_arr)):
        str_line = "Case #%d: %d\n" %(i+1, output_arr[i])
        f.write(str_line)
    f.close()

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)

def calculate_input(inpt):
    B   = inpt[0]
    N   = inpt[1]
    Mk  = inpt[2]

    assert(len(Mk) == B)

    mk_lcm          = lcmm(*Mk);
    num_1round      = 0
    num_mk_1round   = []
    all_b_time      = []
    for i in range(0, len(Mk)):
        assert(mk_lcm%Mk[i] == 0)
        cur_1round = mk_lcm/Mk[i]

        num_mk_1round.append(cur_1round);
        num_1round = num_1round + cur_1round

        for r in range (0, cur_1round):
            all_b_time.append([Mk[i]*r, i]);

    assert(num_1round == len(all_b_time))

    reduce_N = N%num_1round
    if reduce_N == 0:
        reduce_N = reduce_N + num_1round

    all_b_time = sorted(all_b_time, key=itemgetter(0,1))

    #print num_1round, reduce_N
    #print all_b_time

    return all_b_time[reduce_N -1][1] + 1

def main(input_fname, output_fname):
    print ">>>>>>>> READ_INPUT"
    input_arr = parse_input(input_fname)
    print "len(input_arr) : %d" %(len(input_arr))
    #print input_arr

    print ">>>>>>>> CALCULATE OUTPUT"
    output_arr = []
    for i in range(0, len(input_arr)):
        output_arr.append(calculate_input(input_arr[i]))
        print "Finish testcase : %d" %(i)

    print ">>>>>>>> WRITE_OUTPUT"
    write_output(output_fname, output_arr)

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-i", type="str", dest="input_fname")

    (options, args) = parser.parse_args()
    if options.input_fname != None:
        i_fname = options.input_fname
        o_fname = options.input_fname + ".out"

        print "INPUT FILE : %s" %(i_fname)
        print "OUTPUT FILE : %s" %(o_fname)

        main(i_fname, o_fname)
