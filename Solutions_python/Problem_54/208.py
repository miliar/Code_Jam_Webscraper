#!/usr/bin/python

"""
  Google Code Jam 2010
  Philfifi  --  http://www.pluc.fr
  All rigths reserved
"""

"""
a = 900000000000000000001: 1669850621 538970365781
b = 800000000000000000001: 3 3 7993 143513 77490135721

diff=100000000000000000000
factor
100000000000000000000: 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5


A=a+k
B=b+k

800000000000000000001+99999999999999999999
A=900000000000000000000

900000000000000000001+99999999999999999999
B=1000000000000000000000

PGCD(A,B) = 100000000000000000000







"""


from math import sqrt
from decimal import *
getcontext().prec = 100

import psyco
psyco.full()

_debug = 0

def PGCD_of_list(a_l):
    index = 1
    pgcd = a_l[0]
    len_list =len(a_l)
    while index < len_list:
        pgcd = PGCD(pgcd, a_l[index])
        index += 1

    return pgcd

def PGCD(A, B):
    a = max(A, B)
    b = min(A, B)
    while True:
        r = a%b
        if r == 0:
            return b
        a=b
        b=r


def solve_case(case_no, N,  s_l   ):
    print "-------------- New case", case_no
#    print s_l

    # Calculate all the differences
    diff_l = [None] * (N-1)

    a = s_l[0]
    index = 1
    while index < N:
        b = s_l[index]
        diff_l[index-1] = abs(a-b)
        a=b
        index += 1

    # Calculate PGCD of the differences
    pgcd = PGCD_of_list(diff_l)
    pgcd_orig = PGCD_of_list(s_l)

#    print "pgcd_diff", pgcd
#    print "pgcd_orig", pgcd_orig

    if pgcd == pgcd_orig:
        return 0


    # check that all number modulo pgcd gives the same value
    target = s_l[0] % pgcd
    index = 1
#    while index < N:
#        assert target == s_l[index] % pgcd, "bad"
#        index += 1

    return pgcd - target


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        all_ = [int(item) for item in fd.readline().split()]
        N = all_[0]
        s_l_tmp = all_[1:]
        s_l = []

        # Make all cases different:
        for k in s_l_tmp:
            if k not in s_l:
                s_l.append(k)

        N = len(s_l)


        # Have read all stuff for this case:
        f_out.write( "Case #%d: %d\n" % (case_no,
                                         solve_case(case_no, N, s_l)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
