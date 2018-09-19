#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Keisuke FUkuda <keisukefukuda@gmail.com>
# Master student in Tokyo Institute of Technology
#

import re,sys

DEBUG = False

def parse_file(f):
    return parse_input(open(f,'r').read())

def parse_input(s):
    lines = re.split(r'\r|\n|\r\n', s)

    T = int(lines[0])
    cases = []

    for t in range(0, T):
        line = lines[t+1]
        
        seq = []

        terms = re.split(r'\s+', line)
        N = int(terms[0])
        terms = terms[1:]

        if not len(terms) % 2 == 0: raise
        
        while len(terms) > 0:
            seq.append( [terms[0], int(terms[1])] )
            terms = terms[2:]

        if not len(seq) == N: raise
        cases.append(seq)

    return (T, cases,)


def other(c):
    if c == 'O': return 'B'
    else: return 'O'

def next_pos(seq, robo):
    for s in seq:
        if s[0] == robo:
            return s[1]
    return 0


# go to the 'goal' position from the 'current' position, but
# can only go 'max_' meters.
# return the new position
def move_to(cur, goal, max_):
    if abs(cur - goal) <= max_:
        return goal

    else:
        return cur + cmp(goal, cur) * max_
    
if __name__ == "__main__":
    if len(sys.argv) <= 1:
        T, cases, = parse_input(sys.stdin.read())
    else:
        T, cases, = parse_file(sys.argv[1])

    case = 1
    
    for c in range(0,T):
        seq = cases[c]
        time = 0
        pos = {'O' : 1, 'B' : 1}
        
        while len(seq) > 0:
            if DEBUG: print "Time %d" % time

            s = seq[0]

            # the robot to push the next button
            robo = s[0]
            # the other one
            othe = other(robo)

            robo_next = s[1]
            othe_next = next_pos(seq, othe)

            robo_dist = abs(pos[robo] - s[1])
            othe_dist = abs(othe_next - pos[othe])

            if DEBUG:
                print "Robot %s is at %d, next pos is %d" % (robo, pos[robo], robo_next)
                print "Robot %s is at %d, next pos is %d" % (othe, pos[othe], othe_next)
            

            if robo_dist + 1 >= othe_dist or othe_next == 0:
                # the other can reach the next button to push while the robo
                # goes and push. So we gain robo_dist seconds.
                pos[robo] = robo_next
                pos[othe] = othe_next
            else:
                # the other cannot reach the next button to push
                pos[othe] = move_to(pos[othe], othe_next, robo_dist + 1)
                pos[robo] = robo_next
                
            time += robo_dist + 1 # secs to go the distance & 1 sec to push the button
            if DEBUG:
                print "Robot %s took %d time to go, and push button" % (robo, robo_dist)
                print "time = %d" % time
                print
            seq = seq[1:]
            
        print "Case #%d: %d" % (c+1, time)
