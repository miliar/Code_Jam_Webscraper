#!/usr/bin/env python

import argparse
import sys
import logging
import os.path as pt

__dir = pt.dirname(pt.realpath(__file__))
# sys.path.insert(0, pt.join(__dir, '../module'))


def solve_bin(x, r, c):
    assert x <= 4 and r <= 4 and c <= 4
    rc_min = min(r, c)
    if (r * c) < x:
        return False
    if (r * c) % x != 0:
        return False
    if x // 2 > rc_min:
        return False

    if x == 1:
        return True
    if x == 2:
        if r % x == 0 or c % x == 0:
            return True
        else:
            return False
    if x == 3:
        if {r, c} == {1, 3}:
            return False
        else:
            return True
    if x == 4:
        if min(r, c) < 3:
            return False
        else:
            return True
    assert False

def solve(x, r, c):
    if solve_bin(x, r, c):
        return 'GABRIEL'
    else:
        return 'RICHARD'


class P4(object):

    def run(self, args):
        name = args[0]
        parser = self.create_parser(name)
        opts = parser.parse_args(args[1:])
        return self.main(name, opts)

    def create_parser(self, name):
        p = argparse.ArgumentParser(
            prog=name,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            description='Description')
        p.add_argument(
            'in_file',
            help='Input file')
        p.add_argument('-o', '--out_file',
                       help='Output file')
        p.add_argument(
            '--verbose',
            help='More detailed log messages',
            action='store_true')
        p.add_argument(
            '--log_file',
            help='Write log messages to file')
        return p

    def main(self, name, opts):
        logging.basicConfig(filename=opts.log_file,
                            format='%(levelname)s (%(asctime)s): %(message)s')
        log = logging.getLogger(name)
        if opts.verbose:
            log.setLevel(logging.DEBUG)
        else:
            log.setLevel(logging.INFO)
        log.debug(opts)

        fin = open(opts.in_file, 'r')
        if opts.out_file is None:
            opts.out_file = sys.stdout
        else:
            fout = open(opts.out_file, 'w')

        ntest = int(fin.readline().strip())
        for t in range(ntest):
            l = fin.readline().strip().split()
            assert len(l) == 3
            l = [int(x) for x in l]
            f = solve(l[0], l[1], l[2])
            print('Case #%d: %s' % (t + 1, f), file=fout)

        if fout is not sys.stdout:
            fout.close()


        return 0


if __name__ == '__main__':
    P4().run(sys.argv)
