#!/usr/bin/env python

import sys

def rpi(teams):
    wp = []
    #print teams
    # Calculate wp for all teams
    for i, t in enumerate(teams):
        wp.append(len(filter(lambda x: x == '1', t))/\
                float(len(filter(lambda x: x != '.', t))))
    #print wp

    owp = []
    # Calculate owp for all teams
    for i, t in enumerate(teams):
        wpj = []
        # Calculate wp for opponents teams
        for j, op in enumerate(teams):
            if j == i or t[j] == '.':
                continue
            won = played = 0
            for k, game in enumerate(op):
                if k == i or game == '.':
                    continue
                played += 1
                if game == '1':
                    won += 1
            wpj.append(won/float(played))
        owp.append(sum(wpj)/float(len(wpj)))
    #print owp

    oowp = []
    # Calculate oowp for all teams
    for i, t in enumerate(teams):
        sops = 0
        sopsl = 0
        for j, op in enumerate(teams):
            if j == i or t[j] == '.':
                continue
            sops += owp[j]
            sopsl += 1
        oowp.append(sops/float(sopsl))
    #print oowp

    for i in range(len(teams)):
        print 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]

if __name__ == '__main__':
    ncases = int(sys.stdin.readline())
    for i in range(ncases):
        n = int(sys.stdin.readline())
        teams = []
        for _ in range(n):
            teams.append([x for x in sys.stdin.readline().strip('\n')])
        print 'Case #%d:' % (i + 1)
        rpi(teams)
