#!/usr/bin/python

import os
import sys


def is_n_tidy(n):

    # Split n into list of nums
    digit_list = [int(d) for d in str(n)]
    
    # check that each digit is <= to next one
    for x in xrange(0, len(digit_list) - 1):
        if (digit_list[x] > digit_list[x+1]):
            return False

    return True

def main():
    test_file = "test-tidy.in"
    with open(test_file) as f:
        rows = f.read().splitlines()

    T = rows[0]
    cases = rows[1:]

    # Run for each case
    for x in range(0,int(T)):
        
        N = int(cases[x])
        flag = 0        

        while True:
            if (is_n_tidy(N)):
                break
            N = N -1            

        print "Case #{}: {}".format(x+1, N)


if __name__ == "__main__":
    main()
