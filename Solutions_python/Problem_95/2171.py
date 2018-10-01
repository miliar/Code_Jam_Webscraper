#!/usr/bin/env python

from string import maketrans

def solve(i):
    line = raw_input()
    trans = maketrans("abcdefghijklmnopqrstuvwxyz", "yhesocvxduiglbkrztnwjpfmaq")
    print 'Case #%d: %s' % (i + 1, line.translate(trans))

def main():
    n = int(raw_input())
    for i in xrange(n):
        solve(i)

if __name__ == '__main__':
    main()