#!/usr/bin/python

"""
  Google Code Jam 2009
  Philfifi  --  http://www.pluc.fr
  All rigths reserved
"""

from math import sqrt
from decimal import *
getcontext().prec = 100

import psyco
psyco.full()

_debug = 0



def get_permutations(in_l):
    """ Return a list of all permutation of the input list"""
    nb_items = len(in_l)
    if nb_items == 2:
        a = in_l[0]
        b = in_l[1]
        out_l = [[a,b], [b,a]]

    elif nb_items == 1:
        return [in_l]

    else:
        out_l = []
        perm_l = get_permutations(in_l[:-1])
        to_add = in_l[-1]

        for a_perm in perm_l:
            for i in range(nb_items):
                new_perm = a_perm[:]
                new_perm.insert(i, to_add)
                out_l.append(new_perm)

    return out_l

def release_one(P, prison_l, released):
    """ return new prison, gold needed"""
    nb_gold = 0

    #look left
    left_good = released > 0
    look_cell = released -1
    while left_good:
        if prison_l[look_cell]:
            nb_gold += 1
            look_cell -= 1
            if look_cell < 0:
                left_good = False
        else:
            left_good = False

    nb_gold_left = nb_gold

#    print "left", nb_gold

    #look righ
    right_good = released < P-1
    look_cell = released+1
    while right_good:
        if prison_l[look_cell]:
            nb_gold += 1
            look_cell += 1
            if look_cell > P-1:
                right_good = False
        else:
            right_good = False

    prison_l[released] = 0

#    print "right", nb_gold - nb_gold_left
#    print "toto", nb_gold

    return prison_l, nb_gold




def solve_case(case_no, P, Q, release_l    ):
    print "-------------- New case", case_no


#    print release_l
#    print get_permutations(release_l)


    min_gold = None

    for a_permut in get_permutations(release_l):
        # Test a new solution
        prison_l = [1] * P
        all_gold = 0
        for a_release in a_permut:
            prison_l, nb_gold_this_day = release_one(P, prison_l, a_release)
#            print prison_l, nb_gold_this_day
            all_gold += nb_gold_this_day

        if min_gold is None or all_gold < min_gold:
            min_gold = all_gold

    return min_gold


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        P, Q = [int(item) for item in fd.readline().split()]

        release_l = [int(item)-1 for item in fd.readline().split()]


        # Have read all stuff for this case:
        f_out.write( "Case #%d: %d\n" % (case_no,
                                         solve_case(case_no, P, Q, release_l)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
