#!/usr/bin/env python

# standard library imports
from collections import Counter
from contextlib import closing
import logging
from multiprocessing import Pool
import sys

# third party related imports

# local library imports


# logging.basicConfig(level=logging.DEBUG)


class Quaternion(object):

    def __init__(self, symbol, sign=1):

        self.symbol = symbol
        self.sign = sign

    def __str__(self):

        sign = '' if self.sign == 1 else '-'
        return 'Q(' + sign + self.symbol + ')'

    def __eq__(self, other):

        return self.symbol == other.symbol and self.sign == other.sign

    def __ne__(self, other):

        return not self == other

    def __mul__(self, other):

        sign = self.sign * other.sign

        if self.symbol == '1':
            return Quaternion(other.symbol, sign)

        elif other.symbol == '1':
            return Quaternion(self.symbol, sign)

        elif self.symbol == other.symbol:
            return Quaternion('1', sign * -1)

        elif self.symbol == 'i':
            if other.symbol == 'j':
                return Quaternion('k', sign)
            else:
                return Quaternion('j', sign * -1)
        elif self.symbol == 'j':
            if other.symbol == 'i':
                return Quaternion('k', sign * -1)
            else:
                return Quaternion('i', sign)
        else:
            if other.symbol == 'i':
                return Quaternion('j', sign)
            else:
                return Quaternion('i', sign * -1)


def solve(test_case):

    L, X, line = test_case

    if L * X < 3:
        logging.debug('L * X < 3')
        return 'NO'

    cnt = Counter(line)
    if (
        (cnt['i'] == 0 and cnt['j'] == 0) or
        (cnt['i'] == 0 and cnt['k'] == 0) or
        (cnt['j'] == 0 and cnt['k'] == 0)
    ):
        logging.debug('Only one character')
        return 'NO'

    q = Quaternion('1')
    for s in line:
        q = q * Quaternion(s)
        logging.debug('q = %s', q)

    base = q
    for i in xrange(X - 1):
        q = base * q

    if q != Quaternion('1', -1):
        logging.debug('line**X %s != -1', q)
        return 'NO'

    complete_line = line * X
    logging.debug('complete_line = %s', complete_line)
    Q1, QI, QJ, QK = map(Quaternion, '1ijk')
    qi = Quaternion('1')

    for i in xrange(len(complete_line)):
        q = qi * Quaternion(complete_line[i])
        logging.debug('%s * %s = %s', qi, Quaternion(complete_line[i]), q)

        if q != QI:
            qi = q
            continue

        qi = q
        logging.debug('%s|%s', complete_line[:i + 1], complete_line[i + 1:])
        qj = Quaternion('1')
        for j in xrange(i + 1, len(complete_line)):
            q = qj * Quaternion(complete_line[j])
            logging.debug('%s * %s = %s', qj, Quaternion(complete_line[j]), q)

            if q != QJ:
                qj = q
                continue

            qj = q
            logging.debug('%s|%s|%s', complete_line[:i + 1],
                          complete_line[i + 1:j + 1], complete_line[j + 1:])
            qk = Quaternion('1')
            for k in xrange(j + 1, len(complete_line)):
                q = qk * Quaternion(complete_line[k])
                logging.debug('%s * %s = %s', qk, Quaternion(complete_line[k]), q)
                qk = q

            if qk == Quaternion('k'):
                return 'YES'

    return 'NO'


def main(argv):

    if len(argv) != 2:
        print 'usage: python %s input' % argv[0]
        exit(1)

    test_cases = []
    with closing(open(argv[1])) as f:
        num_test_case = int(f.readline())

        for i in xrange(num_test_case):
            L, X = map(int, f.readline().strip().split())
            line = f.readline().strip()
            test_cases.append([L, X, line])

    """
    for ix, test_case in enumerate(test_cases):
        print 'Case #%s: %s' % (ix + 1, solve(test_case))

    """
    p = Pool(4)
    outcomes = p.map(solve, test_cases)
    for ix, outcome in enumerate(outcomes):
        print 'Case #%s: %s' % (ix + 1, outcome)

if __name__ == '__main__':

    main(sys.argv)

    """
    for s in '1ijk':
        assert Quaternion(s) == Quaternion(s)
        assert Quaternion(s, -1) != Quaternion(s)

    for s1 in '1ijk':
        for s2 in '1ijk':
            assert (Quaternion(s1) == Quaternion(s2)) == (s1 == s2)

    for s1 in '1ijk':
        for s2 in '1ijk':
            for s3 in '1ijk':
                assert Quaternion(s1) * (Quaternion(s2) * Quaternion(s3)) == (Quaternion(s1) * Quaternion(s2)) * Quaternion(s3)

    assert Quaternion('1') * Quaternion('1') == Quaternion('1')
    assert Quaternion('1') * Quaternion('i') == Quaternion('i')
    assert Quaternion('1') * Quaternion('j') == Quaternion('j')
    assert Quaternion('1') * Quaternion('k') == Quaternion('k')
    assert Quaternion('i') * Quaternion('1') == Quaternion('i')
    assert Quaternion('i') * Quaternion('i') == Quaternion('1', -1)
    assert Quaternion('i') * Quaternion('j') == Quaternion('k')
    assert Quaternion('i') * Quaternion('k') == Quaternion('j', -1)
    assert Quaternion('j') * Quaternion('1') == Quaternion('j')
    assert Quaternion('j') * Quaternion('i') == Quaternion('k', -1)
    assert Quaternion('j') * Quaternion('j') == Quaternion('1', -1)
    assert Quaternion('j') * Quaternion('k') == Quaternion('i')
    assert Quaternion('k') * Quaternion('1') == Quaternion('k')
    assert Quaternion('k') * Quaternion('i') == Quaternion('j')
    assert Quaternion('k') * Quaternion('j') == Quaternion('i', -1)
    assert Quaternion('k') * Quaternion('k') == Quaternion('1', -1)
    """
