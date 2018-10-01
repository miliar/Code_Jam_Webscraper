#!/usr/bin/python

import sys

def Process(n, line, d):
    print >>sys.stdout, "Case #%d:" % n,
    cline = []
    for l in line:
        cline.append(d[l])
    print "".join(cline)

if __name__ == "__main__":
    d = {}
    d[' '] = ' '
    d['a'] = 'y'
    d['b'] = 'h'
    d['c'] = 'e'
    d['d'] = 's'
    d['e'] = 'o'
    d['f'] = 'c'
    d['g'] = 'v'
    d['h'] = 'x'
    d['i'] = 'd'
    d['j'] = 'u'
    d['k'] = 'i'
    d['l'] = 'g'
    d['m'] = 'l'
    d['n'] = 'b'
    d['o'] = 'k'
    d['p'] = 'r'
    d['q'] = 'z'
    d['r'] = 't'
    d['s'] = 'n'
    d['t'] = 'w'
    d['u'] = 'j'
    d['v'] = 'p'
    d['w'] = 'f'
    d['x'] = 'm'
    d['y'] = 'a'
    d['z'] = 'q'

    n = 0
    for line in sys.stdin:
        if n > 0:
            Process(n, line.strip(), d)


        n += 1
