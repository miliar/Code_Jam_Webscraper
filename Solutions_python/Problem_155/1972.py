# coding=utf-8
"""
Created on 11/04/2015
Code Jam 2015 QR Problem A
@author: manolo
"""

import sys

ifile = sys.stdin
ofile = open('./a.out', 'w')


def r():
    return ifile.readline()[:-1]


def w(case, what):
    ofile.write('Case #{}: {}\n'.format(case, what))


def invite(max_s, s):
    friends = 0
    standing = 0

    for shyness, amount_of_people in enumerate(s):

        if standing < shyness:
            friends += shyness - standing
            standing = shyness

        standing += amount_of_people

    return friends


T = int(r())
for case in range(1, T + 1):
    max_s, s = r().split(' ')

    n = invite(int(max_s), map(int, s))

    w(case, n)

ofile.close
