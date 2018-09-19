# -*- coding: utf-8 -*-

import sys

def calc_wp(games):
    return float(len([i for i in games if i == '1'])) / float(len([i for i in games if i != '.']))

def calc_owp(lines, idx, N):
    owp = 0
    l = 0
    games = lines[idx]
    for i in xrange(0, N):
        if games[i] != '.':
            g = lines[i]
            g = g[:idx] + g[idx+1:]
            owp += calc_wp(g)
            l += 1
    if l > 0:
        owp = owp / l
    return owp

def calc_oowp(games, N, OWPs):
    oowp = 0
    l = 0
    for i in xrange(0, N):
        if games[i] != '.':
            oowp += OWPs[i]
            l += 1
    return oowp / l

def solve_case(lines):
    WPs = {}
    OWPs = {}
    OOWPs = {}
    N = len(lines) if lines else 0
    for i in xrange(0, N):
        WPs[i] = calc_wp(lines[i])
    for i in xrange(0, N):
        OWPs[i] = calc_owp(lines, i, N)
    for i in xrange(0, N):
        OOWPs[i] = calc_oowp(lines[i], N, OWPs)
    r = []
    for i in xrange(0, N):
        r.append(0.25 * WPs[i] + 0.5 * OWPs[i] + 0.25 * OOWPs[i])
    return r

def read_case(lines):
    new_lines = []
    for l in lines:
        new_lines.append([i for i in l])
    return [new_lines]

def read_input(fname):
    fin = open(fname)
    if fin:
        T = int(fin.readline().strip())
        for i in range(0, T):
            lst = []
            N = int(fin.readline().strip())
            for j in range(0, N):
                lst.append(fin.readline().strip())
            yield lst
    else:
        print 'Can not open file', fname
        raise StopIteration

if __name__ == '__main__':
    if len(sys.argv) == 2:
        fname = sys.argv[1]
        fout = open(fname + '.out', 'w')
        idx = 1
        for case in read_input(fname):
            r = solve_case(*read_case(case))
            fout.write('Case #%s:\n' % idx)
            for i in r:
                fout.write('%s\n' % i)
            idx += 1
    else:
        print 'Invalid arguments number'
