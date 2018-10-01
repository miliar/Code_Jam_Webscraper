#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

class Team(object):
    def __init__(self, id, schedule):
        self.schedule = schedule
        self.id = id
        self.wp = self.calcWP()

    def calcWP(self):
        return self.calcOWPAgainst(-1)

    def calcOWPAgainst(self, n):
        wins = 0
        loses = 0
        for i in xrange(len(self.schedule)):
            if i == n:
                continue
            c = self.schedule[i]
            if c == '1':
                wins += 1
            elif c == '0':
                loses += 1
        a = float(wins)/float(wins+loses)
        #print "%d's OWP for %d : %f" % (self.id, n, a)
        return a

    def calcOWP(self, teams):
        total = float(0)
        num = 0
        for i in xrange(len(self.schedule)):
            if self.schedule[i] != '.':
                total += teams[i].calcOWPAgainst(self.id)
                num += 1
        return total/float(num)

    def calcOOWP(self, teams):
        total = float(0)
        num = 0
        for i in xrange(len(self.schedule)):
            if self.schedule[i] != '.':
                total += teams[i].owp
                num += 1
        return total/float(num)

    def calcRPI(self):
        return 0.25*self.wp + 0.50 * self.owp + 0.25 * self.oowp

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for t in range(num_of_case):
        num_of_teams = int(f.readline())
        teams = []
        for n in range(num_of_teams):
            teams.append(Team(n, f.readline().rstrip()))

        print "Case #%d:" % (t+1)
        for team in teams:
            team.owp = team.calcOWP(teams)
            #print "%f,%f" % (team.wp, team.owp)
        for team in teams:
            team.oowp = team.calcOOWP(teams)
        for team in teams:
            team.rpi = team.calcRPI()
            print "%.10f" % (team.rpi)

# sort by key
# for k,v in sorted(d.items())
# sort by value
# for k,v in sorted(d.items(), key=lambda x:x[1])
# items() return tapple, tapple[0] is k, tapple[1] is v
#
# import copy
# copy.copy()
# copy.deepcopy()
#
# a = [0]*100
#

