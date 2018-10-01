#!/usr/bin/python2

import sys

f = open(sys.argv[1], 'r')
lines = f.readlines()
T = int(lines.pop(0)[:-1])
for t_no in range(1, T + 1):
    N = int(lines.pop(0))
    sol = 0
    teams = lines[:N]
    del lines[:N]
    teams = [c.replace(".","2") for c in teams]
    teams = map(str.strip, teams)
    # teams = [[int(x) for x in t] for t in teams]
    l = []
    for t in teams:
        l2 = []
        for c in t:
            l2.append(int(c))
        l.append(l2)
    
    played = [len(team) - team.count(2) for team in l]
    winned = [team.count(1) for team in l]
    opponents = []
    for team in l:
        opponents.append([i for i in range(len(team)) if team[i] != 2])

    wp = [winned[i]/float(played[i]) for i in range(len(l))]
    owp = []

    for i in range(len(l)):
        suma = 0.0
        # import ipdb; ipdb.set_trace()
        for j in opponents[i]:
            suma += (winned[j] - l[j][i]) / float(played[j]-1)
        owp.append(suma/float(len(opponents[i])))

    oowp = []
    for i in range(len(l)):
        suma = 0
        for j in opponents[i]:
            suma += owp[j]
        oowp.append(suma/float(len(opponents[i])))

    print 'Case #%s:' % (t_no)
    for i in range(len(l)):
        print 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]
