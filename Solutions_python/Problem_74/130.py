#! /usr/bin/python

import sys, itertools

def getline():
    return sys.stdin.readline().strip()

def out(s):
    if False:
        print s

def solve(casenum):
    instructions = getline().split()
    todo = { 'B': [], 'O': [], 'both': [], 'pB': 1, 'pO': 1 }
    N = int(instructions[0])
    for i in range(N):
        c = instructions[i * 2 + 1]
        b = int(instructions[i * 2 + 2])
        todo[c].append(b)
        todo['both'].append((c, b))

    t = 0
    out(todo)
    while todo['both']:
        out(t)
        t += 1
        c = todo['both'][0][0]
        b = todo['both'][0][1]
        if todo['p' + c] == b:          # positioned at the correct button
            todo['both'].pop(0)
            todo[c].pop(0)
            pushed = True
        else:
            pushed = False

        for x in ('B', 'O'):
            if x == c and pushed:
                out('%s pushed button %d' % (c, b))
                continue                # "turn" taken up by pushing button
            if not todo[x]:
                out('%s is done' % (x,))
                continue                # this color is out of instructions
            if todo['p' + x] < todo[x][0]:
                out('%s moves from %d to %d' % (x, todo['p' + x], todo['p' + x] + 1))
                todo['p' + x] += 1
            elif todo['p' + x] > todo[x][0]:
                out('%s moves from %d to %d' % (x, todo['p' + x], todo['p' + x] - 1))
                todo['p' + x] -= 1
            else:
                out('%s waits at %d' % (x, todo['p' + x]))
                pass                    # waiting at button

        out("\n")

    print 'Case #%d: %d' % (casenum, t)

cases = int(getline())
for case in xrange(cases):
    solve(case + 1)
