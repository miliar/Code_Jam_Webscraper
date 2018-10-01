# -*- coding: utf-8 -*-
import sys

T = int(raw_input())

for t in xrange(1, T+1):
    sequence = raw_input().split(" ")[1:]
    
    turns = []
    buttons = {}
    position = {}
    for robot in ['O', 'B']:
        buttons[robot] = []
        position[robot] = 1
    
    for robot, button in [sequence[i:i+2] for i in range(0, len(sequence), 2)]:
        turns.append(robot)
        buttons[robot].append(int(button))
            
    seconds = 0
    while len(turns) > 0:
        seconds += 1
        nobody_pressed = True
        for robot in ['O', 'B']:
            if len(buttons[robot]) > 0:
                if position[robot] < buttons[robot][0]:
                    position[robot] += 1
                elif position[robot] > buttons[robot][0]:
                    position[robot] -= 1
                elif (position[robot] == buttons[robot][0]) and (turns[0] == robot) and nobody_pressed:
                    buttons[robot].pop(0)
                    turns.pop(0)
                    nobody_pressed = False
        
    print "Case #%d: %d" % (t, seconds)