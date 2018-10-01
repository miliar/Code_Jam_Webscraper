#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vi:ts=4 sw=4 et

from __future__ import division
from __future__ import print_function

import string
import sys


class Team(object):
    def __init__(self, index):
        self.index = index
        self.matches = 0
        self.wins = 0
        self._OWP = None
        self._OOWP = None

    def WP(self):
        return self.wins / self.matches

    def OWP(self):
        if self._OWP is None:
            raise NotImplementedError()
        return self._OWP

    def OOWP(self):
        if self._OOWP is None:
            raise NotImplementedError()
        return self._OOWP

    def RPI(self):
        return 0.25 * self.WP() + 0.50 * self.OWP() + 0.25 * self.OOWP()


def run_testcase():
    global M
    N = int(raw_input().strip())
    M = [raw_input().strip() for i in range(N)]
    teams = [ Team(i) for i in range(N) ]

    #print(M)

    # WP
    for team in teams:
        for c in M[team.index]:
            if c == '0':
                team.matches += 1
            elif c == '1':
                team.wins += 1
                team.matches += 1
        #print("{0} has WP = {1}".format(string.ascii_uppercase[team.index], team.WP()))

    # OWP
    for team in teams:
        matches = 0
        wins = 0
        OWP = 0.0
        count = 0
        for other in teams:
            if other is not team and M[team.index][other.index] != '.':
                # 'other' is one of my opponents
                count += 1
                wins = other.wins
                if M[other.index][team.index] == '1':
                    wins -= 1
                OWP += wins / (other.matches - 1)
        team._OWP = OWP / count
        #print("{0} has OWP = {1}".format(string.ascii_uppercase[team.index], team.OWP()))

    # OOWP
    for team in teams:
        OOWP = 0.0
        count = 0
        for other in teams:
            if other is not team and M[team.index][other.index] != '.':
                # 'other' is one of my opponents
                count += 1
                OOWP += other.OWP()
        team._OOWP = OOWP / count
        #print("{0} has OOWP = {1}".format(string.ascii_uppercase[team.index], team.OOWP()))

    for team in teams:
        print(team.RPI())


max_testcases = int(raw_input().strip())
for T in range(1, max_testcases+1):
    print("Case #{0}:".format(T))
    run_testcase()
