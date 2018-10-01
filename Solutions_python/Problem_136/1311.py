#!/usr/bin/env python

import sys

def main(in_stream, out_stream):
    n_cases = int(in_stream.next())
    for i in xrange(1, n_cases+1):
        c, f, x = map(float, in_stream.next().split())
        cps = 2
        t_best = x / cps
        t_fac = 0.
        while True:
            t_fac += c / cps
            cps += f
            t = t_fac + x / cps
            if t > t_best:
                break
            t_best = t
        out_stream.write('Case #%d: %.7f\n' % (i, t_best))

if __name__ == '__main__':
    main(sys.stdin, sys.stdout)
