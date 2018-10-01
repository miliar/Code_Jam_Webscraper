#!/usr/bin/python2

"""
  Google Code Jam 2011
  Philfifi  --  http://www.pluc.fr
  All rigths reserved
"""

from math import sqrt
from decimal import *
getcontext().prec = 100

try:
    import psyco
    psyco.full()
except:
    pass

_debug = 0



import operator


def solve_case(case_no, nb_candy, candy_l ):
    print "-------------- New case", case_no

    if reduce(operator.xor, candy_l) != 0:
        return "NO"

    candy_l.sort()
    candy_l.reverse()

    ret= None
    on_test = 0

    case_test = 2**(nb_candy)
    while case_test > 0:
        case_test -= 1
        case = case_test
#        print "test case", case
        values_l = candy_l[:]
        A = []
        B = []
        while values_l:
            item = values_l.pop()
            case, reminder = divmod(case, 2)
            if reminder:
                A.append(item)
            else:
                B.append(item)


        if len(A) >0 and len(B)> 0:
#            print A, B

            A_xor = reduce(operator.xor, A)
            B_xor = reduce(operator.xor, B)

            if A_xor == B_xor:
                # Patrick happy

                max_val = max(sum(A),
                              sum(B))
                if ret is None:
                    ret = max_val
                    return ret
                else:
                    m = max(ret,
                            max_val)


    return ret


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        nb_candy = int(fd.readline().strip())
        values_l = [int(item) for item in fd.readline().split()]

        assert len(values_l) == nb_candy, "What ? %d %d" % (len(values_l), nb_candy)

        # Have read all stuff for this case:
        f_out.write( "Case #%d: %s\n" % (case_no,
                                         solve_case(case_no, nb_candy, values_l)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
