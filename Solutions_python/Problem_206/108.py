#!/usr/bin/env python
from __future__ import unicode_literals
import decimal
import fractions
import sys


def main(argv=sys.argv):
    infile = argv[1]
    outfile = argv[2]
    with open(infile) as f, open(outfile, 'w') as g:
        T = int(f.readline().strip())
        
        for case in xrange(1, T+1):
            D, N = map(int, f.readline().strip().split())

            fracs = []
            for _ in xrange(N):
                k, s = map(int, f.readline().strip().split())
                fracs.append(fractions.Fraction(D-k, s))
            latest_time = max(fracs)
            speed = D / latest_time
            result = decimal.Decimal(speed.numerator) / decimal.Decimal(speed.denominator)
            g.write("Case #{}: {}\n".format(case, result))
    return 0

if __name__ == "__main__":
    status = main(argv=sys.argv)
    sys.exit(status)
