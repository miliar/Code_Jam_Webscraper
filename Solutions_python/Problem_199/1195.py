import sys
#import matplotlib.pyplot as plt
import numpy as np
from scipy.special import comb
#import scipy as sp
import itertools
from string import maketrans

DISPLAY_RESULTS = False

def solve(S,K):
    intab='-+'
    outtab='+-'
    trantable = maketrans(intab, outtab)
    result = 0

    for pos in range(len(S)-K+1):
        if S[pos] == '-':
            if DISPLAY_RESULTS:
                print(S)
            S = S[:pos] + S[pos:pos+K].translate(trantable) + S[pos+K:]
            result += 1
            if DISPLAY_RESULTS:
                print("--> " + S)

    if S.find('-') != -1:
        result = "IMPOSSIBLE"

    return result


def solveAll(input, output=sys.stdout, case=None):
    T = int(input.readline())
    for case in xrange(T):
        S,K = input.readline().strip().split(' ')
        K = int(K)

        result= "Case #%d: %s\n" % (case + 1, solve(S,K))
        output.write(result)
        if output != sys.stdout:
            sys.stdout.write(result)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        in_fd = open(sys.argv[1])
        out_fd = open(sys.argv[1].replace('input','output'),'w')
        solveAll(in_fd, out_fd)
        out_fd.close()
        in_fd.close()
    else:
        solveAll(sys.stdin)