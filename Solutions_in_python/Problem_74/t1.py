#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

def next_position(actions, c, default):
    for action in actions:
        if action[0] == c:
            return action[1]
    return default

def advance(value, direction):
    if direction > 0:
        return value
    elif direction < 0:
        return -value
    else:
        return 0

def solve(line):
    line = line.split()

    actions = []
    for i in xrange(len(line)/2):
        actions.append((line[2*i+1], int(line[2*i+2])))

    bcur = 1
    ocur = 1
    ret = 0
    while actions:
        onext = next_position(actions, 'O', ocur)
        bnext = next_position(actions, 'B', bcur)

        dist = min(abs(onext - ocur), abs(bnext - bcur))

        ocur += advance(dist, onext - ocur)
        bcur += advance(dist, bnext - bcur)
        ret += dist

        if actions[0][0] == 'O':
            ret += abs(onext - ocur) + 1
            ocur = onext
            bcur += advance(1, bnext - bcur)
        else:
            ret += abs(bnext - bcur) + 1
            bcur = bnext
            ocur += advance(1, onext - ocur)
        actions = actions[1:]

    return ret

def main():
    T = int(sys.stdin.readline())
    for i in xrange(T):
        ret = solve(sys.stdin.readline())
        print "Case #" + str(i+1) + ": " + str(ret)

if __name__ == '__main__':
    main()
