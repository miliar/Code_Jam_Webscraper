#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4 et sw=4

from __future__ import print_function

import string

english_ab    = string.ascii_lowercase
googlerese_ab = 'y             e          q'

def get_alphabet_from_samples(samples):
    global googlerese_ab

    for g, e in samples.items():
        for i in xrange(len(g)):
            if e[i].isspace():
                continue

            idx = ord(e[i]) - ord('a')
            if googlerese_ab[idx] == ' ':
                googlerese_ab = g[i].join([googlerese_ab[:idx],
                    googlerese_ab[idx+1:]])
            elif googlerese_ab[idx] != g[i]:
                raise Exception('non-unique mapping')

    remainder = english_ab
    for i in xrange(len(remainder)):
        if googlerese_ab[i] != ' ':
            remainder = remainder.replace(googlerese_ab[i], ' ')

    remainder = remainder.replace(' ', '')
    
    if len(remainder) != 1:
        raise Exception('more than one remaining character')
    else:
        googlerese_ab = googlerese_ab.replace(' ', remainder)

def main():
    samples = {
        'ejp mysljylc kd kxveddknmc re jsicpdrysi': 'our language is impossible to understand',
        'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd': 'there are twenty six factorial possibilities',
        'de kr kd eoya kw aej tysr re ujdr lkgc jv': 'so it is okay if you want to just give up',
    }

    get_alphabet_from_samples(samples)
    trans_table = string.maketrans(googlerese_ab, english_ab)

    test_cases = int(raw_input())

    for i in xrange(1, test_cases + 1):
        s = raw_input()

        english = s.translate(trans_table)

        print('Case #{0}: {1}'.format(i, english))

if __name__ == '__main__':
    main()
