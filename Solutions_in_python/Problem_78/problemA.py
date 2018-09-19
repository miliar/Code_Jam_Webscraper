from __future__ import division, print_function


import fractions

def run(input, output, verbose=False):
    T = int(input.readline())
    for index in xrange(1, T + 1):
        [N, Pd, Pg] = [int(x) for x in input.readline().strip().split()]
        if verbose:
            print("#%d %d %d %d" % (index, N, Pd, Pg))
        invgcd = 100 // fractions.gcd(Pd, 100)
        if N < invgcd:
            if verbose:
                print("N < invgcd : %d < %d" % (N, invgcd))
            res = False
        elif (Pd < 100) and (Pg == 100):
            if verbose:
                print("Pd < 100, Pg = 100 : %d %d" % (Pd, Pg))
            res = False
        elif (Pd > 0) and (Pg == 0):
            if verbose:
                print("Pd < 100, Pg = 100 : %d %d" % (Pd, Pg))
            res = False
        else:
            res = True
        print("Case #%d: %s" % (index, "Possible" if res else "Broken"), file=output)

