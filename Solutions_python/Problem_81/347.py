# -*- coding: utf-8 -*-

from collections import defaultdict

def WP(i, wins, loses):
    v = 1.0 * len(wins[i]) / (len(wins[i]) + len(loses[i]))
    return v

def OWP(i, wins, loses):
    acc = 0.0
    length = len(wins[i]) + len(loses[i])
    for o in wins[i]:
        size = len(wins[o])
        if i in wins[o]:
            size -= 1
        acc += (1.0 * size / (len(wins[o]) + len(loses[o]) - 1))
    for o in loses[i]:
        size = len(wins[o])
        if i in wins[o]:
            size -= 1
        acc += (1.0 * size / (len(wins[o]) + len(loses[o]) - 1))
    #TODO division by zero?
    return acc / length

def OOWP(i, wins, loses, owp):
    acc = 0.0
    for o in wins[i]:
        acc += owp[o]
    for o in loses[i]:
        acc += owp[o]
    length = len(wins[i]) + len(loses[i])
    #TODO division by zero?
    return acc / length

#def RPI(i, wins, loses, winning_percentage, opponents_winning_percentage):
#    RPI = 0.25 * winning_percentage[i] + 0.50 * opponents_winning_percentage(i) + 0.25 * OOWP(i, wins, loses)
#    return RPI

def doit():
    N = input()
    wins = defaultdict(set)
    loses = defaultdict(set)
    for x in xrange(N):
        line = list(raw_input())
        for y in xrange(N):
            v = line[y]
            if v == '0':
                loses[x].add(y)
                wins[y].add(x)
            elif v == '1':
                loses[y].add(x)
                wins[x].add(y)
    
    wp = {}
    for i in xrange(N):
        wp[i] = WP(i, wins, loses)
        
    owp = {}
    for i in xrange(N):
        owp[i] = OWP(i, wins, loses)
    
    oowp = {}
    for i in xrange(N):
        oowp[i] = OOWP(i, wins, loses, owp)


    for i in xrange(N):
        print 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]
    
    
    
T = input()

for t in xrange(1, T+1):
    print 'Case #%d:' % t
    doit()
