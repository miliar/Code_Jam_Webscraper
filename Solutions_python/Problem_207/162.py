#!/usr/bin/env python
""" template.py input-file > output-file"""

import sys
from numpy import *

sys.setrecursionlimit(10000)

def input_words():
    line = IN.readline()
    return line.strip().split()

def input_ints():
    return map(int, input_words())

def input_floats():
    return map(float, input_words())

def format_sequence(s, formatter='%s'):
    return " ".join(map(lambda x: formatter % (x,), s))


def solve(N, R, O, Y, G, B, V):
    assert N == R + O + Y + G + B + V
    inventory = {}
    for k, v in {'R': R, 'O': O, 'Y': Y, 'G': G, 'B': B, 'V': V}.iteritems():
        inventory[k] = [k] * v
        
    #print inventory
    if N == 1:
        for k, v in inventory.iteritems():
            if len(v) > 0: 
                return k
#    if N < 3: 
#        raise 'special case it'
        
    dual_needed = {'G': 'R', 'O': 'B', 'V': 'Y'}
    for weird, good in dual_needed.iteritems():
        while len(inventory[weird]) > 0:
            if len(inventory[good]) < 2:
                if sum([len(v) for v in inventory.values()]) == 2 and (
                    len(inventory[good]) == 1):
                    #import pdb; pdb.set_trace()
                    return inventory[weird][0] + inventory[good][0]
                else: 
                    return 'IMPOSSIBLE'
            else:
                i1 = inventory[good].pop()
                i2 = inventory[weird].pop()
                i3 = inventory[good].pop()
                inventory[good].append(i1 + i2 + i3)
        del inventory[weird]
    
    good_colors = ['R', 'Y', 'B']
    reduced_N = sum([len(inventory[x]) for x in good_colors])
    for x in good_colors:
        if len(inventory[x]) * 2 > reduced_N:
            #print 'balance fail', reduced_N, inventory
            #import pdb; pdb.set_trace()
            return 'IMPOSSIBLE'
        
    while True:
        mm = min([len(inventory[x]) for x in good_colors])
        if len(inventory['R']) == mm:
            tgt1, tgt2, last = 'Y', 'B', 'R'
        elif len(inventory['Y']) == mm:
            tgt1, tgt2, last = 'R', 'B', 'Y'
        elif len(inventory['B']) == mm:
            tgt1, tgt2, last = 'Y', 'R', 'B'
        
        if len(inventory[tgt1]) < len(inventory[tgt2]):
            tgt1, tgt2 = tgt2, tgt1
        
#        print mm, tgt1, tgt2, inventory

        if len(inventory[tgt1]) == 0:
            #print 'A'
            return inventory[tgt2][0]
        elif len(inventory[tgt2]) == 0:
            #print 'B'
            return inventory[tgt1][0]
        elif len(inventory[tgt1]) == 1:
            #print 'C'
            assert len(inventory[tgt2]) == 1
            assert len(inventory[last]) <= 1
            if len(inventory[last]) == 0:
                return inventory[tgt1][0] + inventory[tgt2][0]
            else:
                return inventory[tgt1][0] + inventory[tgt2][0] + inventory[last][0]
        
        i1 = inventory[tgt1].pop()
        i2 = inventory[tgt2].pop()
        i3 = inventory[tgt1].pop()
        inventory[tgt1].append(i1 + i2 + i3)
        #print '--->', inventory


def solve_one():
    """ XXX the real code comes here """
    x = map(int, input_words())
    return solve(*x)

if __name__ == "__main__":
    assert(len(sys.argv) == 2)
    IN = open(sys.argv[1])

    T = input_ints()[0]
    
    for i in range(T):
        print "Case #%d:" % (i+1,), solve_one()
        sys.stderr.write("CASE #%d DONE\n" % (i+1,))
        sys.stderr.flush()


