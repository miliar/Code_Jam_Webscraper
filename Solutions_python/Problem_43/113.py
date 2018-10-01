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



def solve_case(case_no, line    ):
    print "-------------- New case", case_no

    len_str = len(line)

    unique_symbols_l = []
    symbols_to_val_d = {}
    for c in line:
        if c not in unique_symbols_l:
            unique_symbols_l.append(c)
            symbols_to_val_d[c] = None

    nb_unique_symbols = len(unique_symbols_l)

    min_base = nb_unique_symbols
    if min_base == 1:
        min_base = 2

    current_symbol_value = 1

    total_value = 0
    for c in line:
        this_value = None
        if symbols_to_val_d[c] is None:
            symbols_to_val_d[c] = current_symbol_value
            print "%s -> %s" % (c, current_symbol_value)
            this_value = current_symbol_value
            if current_symbol_value == 1:
                current_symbol_value = 0
            elif current_symbol_value == 0:
                current_symbol_value = 2
            else:
                current_symbol_value += 1

        else:
            this_value = symbols_to_val_d[c]

        total_value = min_base * total_value + this_value

    return total_value


def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        line = fd.readline()


        # Have read all stuff for this case:
        f_out.write( "Case #%d: %d\n" % (case_no,
                                         solve_case(case_no, line.strip())
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
