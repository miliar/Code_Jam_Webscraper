#!/usr/bin/env python2
# -*- coding: utf-8 -*-


"""
CodeJam2017 / QR / A. Oversized Pancake Flipper
__author__ = 'krikit <krikit@naver.com>'
"""


###########
# imports #
###########
from __future__ import unicode_literals
from __future__ import print_function

import codecs
import logging
logging.basicConfig(level=logging.INFO)
import heapq
import optparse
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')    # pylint: disable=no-member


############
# function #
############
def _solve(S, K):
    flip = 0
    begin = 0
    while True:
        try:
            pos_blank = S.index('-', begin)
        except ValueError:
            return flip
        if len(S) - pos_blank < K:
            return -1
        for k in range(K):
            S[pos_blank + k] = '-' if S[pos_blank + k] == '+' else '+'
        flip += 1
        begin = pos_blank + 1
    return flip


########
# main #
########
def main():
    """
    CodeJam2017 / QR / A. Oversized Pancake Flipper
    """
    for case_num, case in enumerate(sys.stdin):
        if case_num == 0:
            continue
        S, K = case.split()
        answer = _solve(list(S), int(K))
        print('Case #%d: %s' % (case_num, str(answer) if answer >= 0 else 'IMPOSSIBLE'))


if __name__ == '__main__':
    _PARSER = optparse.OptionParser(description='CodeJam2017 / QR / A. Oversized Pancake Flipper')
    _PARSER.add_option('--input', help='input file <default: stdin>', metavar='FILE')
    _PARSER.add_option('--output', help='output file <default: stdout>', metavar='FILE')
    _OPTS, _ = _PARSER.parse_args()
    if _OPTS.input:
        sys.stdin = codecs.open(_OPTS.input, 'rt', encoding='UTF-8')
    if _OPTS.output:
        sys.stdout = codecs.open(_OPTS.output, 'wt', encoding='UTF-8')
    main()
