#!/bin/python

import fileinput
import pdb

T = int(raw_input())
for i in range(T):
    first_row = int(raw_input())
    for j in range(4):
        if j+1 is first_row:
            l1 = map(int, raw_input().split())
        else:
            _ = raw_input()

    second_row = int(raw_input())
    for j in range(4):
        if j+1 is second_row:
            l2 = map(int, raw_input().split())
        else:
            _ = raw_input()
            
    possible_cards = set(l1).intersection(set(l2))
    if len(possible_cards) > 1:
        result = 'Bad magician!'
    elif len(possible_cards) < 1:
        result = 'Volunteer cheated!'
    else:
        result = str(list(possible_cards)[0])
        
    print 'Case #%d: %s' % (i+1, result)