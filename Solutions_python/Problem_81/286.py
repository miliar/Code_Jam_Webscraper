#!/usr/bin/env python3

class Team(object):
    def __init__(self, string):
        self.score = string
        self.won = 0
        self.lost = 0
        self.owp = 0.0
        self.oowp = 0.0
        self.rpi = 0.0

data = open('rpi.in')

for i in range(int(data.readline())):
    teams = list()
    for j in range(int(data.readline())):
        teams.append(Team(data.readline()[:-1]))
    for team in teams:
        for res in team.score:
            if res == '1':
                team.won += 1
            if res == '0':
                team.lost += 1
    for j, team in enumerate(teams):
        perc = 0.0
        for opp in teams:
            if opp.score[j] == '.':
                continue
            else:
                perc += (opp.won - int(opp.score[j])) / (opp.won+opp.lost-1)
        team.owp = perc / (team.won+team.lost)
    for j, team in enumerate(teams):
        perc = 0.0
        for opp in teams:
            if opp.score[j] != '.':
                perc += opp.owp
        team.oowp = perc / (team.won+team.lost)
    for team in teams:
        team.rpi = .25*(team.won/(team.won+team.lost)) + .5*team.owp + .25*team.oowp

    print('Case #%d:' % (i+1))
    for t in teams:
        print(t.rpi)


