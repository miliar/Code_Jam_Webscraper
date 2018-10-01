#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint
import sys

def parse_line(input_):
    input2 = input_.split()
    n_buttons = int(input2[0])
    _buttons = input2[1:]
    buttons = zip(_buttons[::2], [int(b) for b in _buttons[1::2]])
    return n_buttons, buttons

def next_push(b, pushed, buttons):
    next = [x[1] for x in buttons[pushed:] if x[0] == b]
    try:
        return next[0]
    except IndexError:
        return None

def calc_time(line):
    N, buttons = parse_line(line)
    #print "Iniciando...",
    #pprint(buttons)
    timeline = {'O': [], 'B': []}
    position = {'O': 1, 'B': 1}

    pushed = 0
    while pushed < N:
        this_push = buttons[pushed][0]
        next_o = next_push('O', pushed, buttons)
        next_b = next_push('B', pushed, buttons)
        pO = position['O']
        pB = position['B']
        
        if next_o == pO:
            if this_push == 'O':
                timeline['O'].append(('push', pO))
                pushed += 1
            else:
                timeline['O'].append(('stay', pO))
        elif next_o != pO:
            if pO < next_o:
                next_step = pO + 1
            else:
                next_step = pO - 1
            timeline['O'].append(('walk', next_step))
            position['O'] = next_step

        if next_b == pB:
            orange_last_action = timeline['O'][-1][0]
            if this_push != 'B' or orange_last_action == 'push':
                timeline['B'].append(('stay', pB))
            else:
                timeline['B'].append(('push', pB))
                pushed += 1
        elif next_b != pB:
            if pB < next_b:
                next_step = pB + 1
            else:
                next_step = pB - 1
            timeline['B'].append(('walk', next_step))
            position['B'] = next_step

    #print "Resultado:",
    #pprint(timeline)
    
    return max(len(timeline['O']), len(timeline['B']))

def main(input_):
    for i, line in enumerate(input_.split('\n')[1:]):
        if not line:
            continue
        print "Case #%s: %s" % (i+1, calc_time(line))

if __name__ == '__main__':
    main(sys.stdin.read().strip())
