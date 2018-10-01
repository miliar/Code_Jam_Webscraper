#!/usr/bin/env python

import sys
input = sys.stdin

NMax = 500
MOD = 100003

def main():
    comb = [[0 for i in range(NMax + 1)] for j in range(NMax + 1)]
    comb[0][0] = 1
    for i in range(1, NMax + 1):
        comb[i][0] = 1
        for j in range(1, NMax + 1):
            comb[i][j] = (comb[i - 1][j - 1] + comb[i - 1][j]) % MOD

    nr = [[0 for i in range(NMax + 1)] for j in range(NMax + 1)]
    for i in range(2, NMax + 1):
        nr[1][i] = 1
    tot = [1 for i in range(NMax + 1)]
    for i in xrange(2, NMax + 1):
        sys.stderr.write("%d\n" % i)
        for j in xrange(i + 1, NMax + 1):
            nr[i][j] = 0
            for k in xrange(1, i):
                # Pe pozitia i valoarea j
                # Pe pozitia k valoarea i
                # Pe pozitiile (k + 1 ... i - 1) valori intre (i + 1) si (j - 1)

                nr[i][j] = (nr[i][j] + nr[k][i] * comb[(j - 1) - (i + 1) + 1][(i - 1) - (k + 1) + 1]) % MOD
            tot[j] = (tot[j] + nr[i][j]) % MOD

    T = int(input.readline())
    for t in range(1, T + 1):
        N = int(input.readline())
        print "Case #%d: %s" % (t, tot[N])
    return 0

if __name__ == "__main__":
    main()

