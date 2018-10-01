# Has been a great while since I coded...Here Goes
# Snapper
# Usage pretty simple: Q1.py <inputfile>
# requires a EOF to terminate


#Read Input - Absolutely 0 input checks

import fileinput
import fractions

infile = fileinput.input()

p = infile.readline()

N = long(p)

n = 0

while n < N:
    n += 1
    params = infile.readline()
    C = [long(p) for p in params.split()]

    S = C[0]
    del C[0]
    
    if S == 2:
        G = abs(C[0] - C[1])

    if S == 3:
        G1 = abs(C[0] - C[1])
        G2 = abs(C[1] - C[2])
        G3 = abs(C[2] - C[1])
        G = fractions.gcd(fractions.gcd(G1,G2),G3)
    if 0 == C[0]%G:
        X = 0
    else:
        X = G - (C[0] % G)

    
    print "Case #%d: %d" % (n,X)

infile.close()

