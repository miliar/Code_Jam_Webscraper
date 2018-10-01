#! /usr/bin/env python2

import sys

def preprocess(mat):
    res = []
    for n in xrange(len(mat)):
        team_res = {}
        for opp, match_res in enumerate(mat[n]):
            if match_res != '.':
                match_res = (match_res == '1')
                team_res[opp] = match_res
        res.append(team_res)
    return res

def compute_wp(mat, team, wp, exclude=None):
    if exclude not in wp:
        wp[exclude] = {}

    if team in wp[exclude]:
        return wp[exclude][team]

    q = len([x for x in mat[team] if mat[team][x] == True and x != exclude])
    d = float(len([x for x in mat[team] if x != exclude]))
    s = q / d
    wp[exclude][team] = s
    return s

def compute_owp(mat, team, wp, owp):
    if team in owp:
        return owp[team]

    opp_wp = [compute_wp(mat, t, wp, team) for t in mat[team]]
    s = sum(opp_wp) / float(len(opp_wp))
    owp[team] = s
    return s

def compute_oowp(mat, team, wp, owp, oowp):
    if team in oowp:
        return oowp[team]

    opp_owp = [compute_owp(mat, t, wp, owp) for t in mat[team]]
    s = sum(opp_owp) / float(len(opp_owp))
    oowp[team] = s
    return s

def rpi(mat, team, wp, owp, oowp):
    my_wp = compute_wp(mat, team, wp)
    my_owp = compute_owp(mat, team, wp, owp)
    my_oowp = compute_oowp(mat, team, wp, owp, oowp)
    return 0.25 * my_wp + 0.50 * my_owp + 0.25 * my_oowp

def rpi_all(mat):
    wp = {}
    owp = {}
    oowp = {}
    for team in xrange(len(mat)):
        yield rpi(mat, team, wp, owp, oowp)

if __name__ == '__main__':
    T = input()
    for t in xrange(1, T+1):
        N = input()
        mat = [raw_input() for n in xrange(N)]
        mat = preprocess(mat)
        print >>sys.stderr, 'Case #%d:' % t
        print 'Case #%d:' % t
        for res in rpi_all(mat):
            print res
