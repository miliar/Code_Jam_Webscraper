#!/usr/bin/env python
from __future__ import division
import cStringIO
import fileinput


def run(infile=None):
    if infile is None:
        infile = fileinput.input()

    def get_lines(n):
        lines = list()
        for i in xrange(n):
            lines.append(infile.readline())
        return lines

    def solve(n, l, h, freqs):
        ret = set()
        freqs = sorted(freqs)
        f = freqs.pop()
        for i in xrange(l, h+1):
            if f % i == 0 or i % f == 0:
                ret.add(i)

        for i in list(ret):
            for f in freqs:
                if f % i != 0 and i % f != 0:
                    try:
                        ret.remove(i)
                    except KeyError:
                        pass
        
        return 'NO' if not ret else min(ret)

    try:
        cases = int(infile.readline())
    except ValueError:
        print 'Error: Test case count not found'
        return []
    case_results = list()
    for case in xrange(cases):
        lines = get_lines(2)
        n, l, h = map(int, lines[0].strip().split(' '))
        freqs = map(int, lines[1].strip().split(' '))
        case_results.append('Case #%d: %s' % (case+1, 
                    solve(n, l, h, freqs)))
    return case_results

def test():
    expected = [
        'Case #1: NO',
        'Case #2: 10'
    ]

    result = run(cStringIO.StringIO(
        '2\n'
        '3 2 100\n'
        '3 5 7\n'
        '4 8 16\n'
        '1 20 5 2\n'
    ))

    print '\n'.join(result)
    assert expected == result, expected

if __name__ == "__main__":
    print '\n'.join(run())
    #test()
