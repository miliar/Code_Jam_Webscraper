#!/usr/bin/python
import sys

class Team():
    def __init__(self, index, total):
        self.index = index
        self.total = total
        self._WP = None
        self._OWP = None
        self._OOWP = None
        self.opponents = []
    def playsAgainst(self, team):
        return self.total[self.index][team.index] != '.'
    def setupOpponents(self, teams):
        for team in teams:
            if self.playsAgainst(team):
                self.opponents.append(team)
    def WP(self):
        if self._WP != None:
            return self._WP
        won = 0
        lost = 0
        for i, c in enumerate(self.total[self.index]):
            if c == '1':
                won += 1
            elif c == '0':
                lost += 1
        self._WP = won * 1.0 / ((won + lost) * 1.0)
        return self._WP
    def WPminus(self, opponent):
        won = 0
        lost = 0
        for i, c in enumerate(self.total[self.index]):
            if i != opponent.index:
                if c == '1':
                    won += 1
                elif c == '0':
                    lost += 1
        return won * 1.0 / ((won + lost) * 1.0)
    def OWP(self):
        if self._OWP != None:
            return self._OWP
        summ = 0
        for opponent in self.opponents:
            summ += opponent.WPminus(self)
        self._OWP = summ * 1.0 / (1.0 * len(self.opponents))
        return self._OWP
    def OOWP(self):
        if self._OOWP != None:
            return self._OOWP
        summ = 0
        for opponent in self.opponents:
            summ += opponent.OWP()
        self._OOWP = summ * 1.0 / (1.0 * len(self.opponents))
        return self._OOWP
    def RPI(self):
        return 0.25 * self.WP() + 0.50 * self.OWP() + 0.25 * self.OOWP()

def solve(*args):
    teams = []
    for i, arg in enumerate(args):
        teams.append(Team(i, args, ))
    for team in teams:
        team.setupOpponents(teams[:])
    return [team.RPI() for team in teams]

if __name__ == "__main__":
    lines = input()
    i = 0
    output = []
    while i < lines:
        groups = input()
        group = []
        j = 0
        while j < groups:
            group.append(raw_input())
            j += 1
        output.append(solve(*group))
        i += 1
    i = 0
    while i < lines:
        print "Case #%i:\n%s" % (i + 1, '\n'.join(map(str, output[i])))
        i += 1
