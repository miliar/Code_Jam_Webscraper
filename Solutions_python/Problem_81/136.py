#!/usr/bin/python -u

import sys
import itertools

def RPI(WP, OWP, OOWP):
    return 0.25 * WP + 0.50 * OWP + 0.25 * OOWP

def average(values):

    # print values
    return sum(values) / float(len(values))


def solveBruteForce(N,matrix):

    # note that matrix is antisymmetric of some kind

    # count number of games of team i
    numGames = []

    for i in range(N):
        numGames.append(len([ x for x in matrix[i] if x != None ]))

    numWins = []

    # calculate WP for team i
    for i in range(N):
        numWins.append(len([ x for x in matrix[i] if x == 1 ]))

    wp = [ wins / float(total) for wins,total in zip(numWins, numGames) ]

    # calculate opponents

    opponents = []

    for i in range(N):

        opponents.append([ j for j in range(N) if matrix[i][j] != None ])
    
    # calculate owp
    # note that we must ignore those games played against i
    owp = []
    for i in range(N):
        wpPrime = [ ]

        for j in range(N):
            # if j played against i, recalculate the wp for this calculation here
            if matrix[i][j] != None:
                if matrix[j][i] == 1:
                    # j won against i
                    wpPrime.append((numWins[j] - 1) / float(numGames[j] - 1))
                else:
                    # j did not win against i
                    wpPrime.append(numWins[j] / float(numGames[j] - 1))
            else:
                # i and j never played
                wpPrime.append(wp[j])
                    
        owp.append(average([wpPrime[j] for j in opponents[i]]))

    # calculate oowp

    oowp = []
    for i in range(N):
        oowp.append(average([ owp[j] for j in opponents[i]]))

    # print "WP=",wp
    # print "OWP=",owp
    # print "OOWP=",oowp
    

    return [ RPI(x,y,z) for x,y,z in zip(wp,owp,oowp) ]
    
    

#----------------------------------------------------------------------

def solveSmart():
    pass



#----------------------------------------------------------------------
# main
#----------------------------------------------------------------------

T = int(sys.stdin.readline())

for case in range(1,T+1):

    N = int(sys.stdin.readline())

    matrix = []

    for i in range(N):

        line = sys.stdin.readline().split('\n')[0]

        data = []
        for x in line:
            if x == '.':
                x = None
            else:
                x = int(x)

            data.append(x)
        
        matrix.append(data)

    #if case != 2:
    #    continue

    sol = solveBruteForce(N,matrix)


    print "Case #%d:" % case

    for s in sol:
        print "%.12f" % s
    
