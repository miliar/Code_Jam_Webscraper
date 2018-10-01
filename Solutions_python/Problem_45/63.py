#!/usr/bin/env python2.6
import sys
from itertools import permutations

def get_bribe(cells, freed):
    c = 0
    j = freed + 1
    while j < len(cells) and cells[j] == 1:
        j += 1
        c += 1
    
    j = freed - 1
    while j >= 0 and cells[j] == 1:
        j -= 1
        c += 1
    return c

def get_bribes(cells, tofree, memo):
    if len(tofree) == 0:
        return 0
    else:
        c = tofree[0]
        remaining = tofree[1:]
        bribe = get_bribe(cells, c)
        try:
            return bribe + memo[tuple(remaining)]
        except KeyError:
            cells[c] = 0
            result = memo[tuple(remaining)] = get_bribes(cells, remaining, memo)
            return result + bribe


def find_min(ncells, tofree):

    min_coins = sys.maxint
    
    memo = {}
    for i in permutations(tofree):
#        print i
        cells = [1 for d in range(ncells)]
        #print i, get_bribes(cells, i, 0, memo)
        min_coins = min(get_bribes(cells, i, memo), min_coins)

   # while tofree:
    #    if ncells - (tofree[-1] + 1) > ncells[0]:
    #        c = -1
    #    else:
    #        c = 0
        
    #    coins += get_bribe(cells, c)
        
    #    for p in [0, len(tofree) - 1]:
    #        pass
            
    #    pass
    return min_coins


with open(sys.argv[1], "r") as f:
    tests = int(f.readline().strip())
    for t in range(tests):
        ncells, released = [int(x) for x in f.readline().strip().split()]
        tofree = [int(x) - 1 for x in f.readline().strip().split()]
        print "Case #%d: %d" % (t+1, find_min(ncells, tofree))


