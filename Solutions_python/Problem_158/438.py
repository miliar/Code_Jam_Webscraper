#!/usr/bin/python
# vi: set fileencoding=utf-8 :

'''
Google code jam 2015 qualification round
D: Ominous Omino
'''

winner_dic = {
        (1, 1, 1): 'GABRIEL',
        (1, 1, 2): 'GABRIEL',
        (1, 1, 3): 'GABRIEL',
        (1, 1, 4): 'GABRIEL',
        (1, 2, 2): 'GABRIEL',
        (1, 2, 3): 'GABRIEL',
        (1, 2, 4): 'GABRIEL',
        (1, 3, 3): 'GABRIEL',
        (1, 3, 4): 'GABRIEL',
        (1, 4, 4): 'GABRIEL',
        (2, 1, 1): 'RICHARD',
        (2, 1, 2): 'GABRIEL',
        (2, 1, 3): 'RICHARD',
        (2, 1, 4): 'GABRIEL',
        (2, 2, 2): 'GABRIEL',
        (2, 2, 3): 'GABRIEL',
        (2, 2, 4): 'GABRIEL',
        (2, 3, 3): 'RICHARD',
        (2, 3, 4): 'GABRIEL',
        (2, 4, 4): 'GABRIEL',
        (3, 1, 1): 'RICHARD',
        (3, 1, 2): 'RICHARD',
        (3, 1, 3): 'RICHARD',
        (3, 1, 4): 'RICHARD',
        (3, 2, 2): 'RICHARD',
        (3, 2, 3): 'GABRIEL',
        (3, 2, 4): 'RICHARD',
        (3, 3, 3): 'GABRIEL',
        (3, 3, 4): 'GABRIEL',
        (3, 4, 4): 'RICHARD',
        (4, 1, 1): 'RICHARD',
        (4, 1, 2): 'RICHARD',
        (4, 1, 3): 'RICHARD',
        (4, 1, 4): 'RICHARD',
        (4, 2, 2): 'RICHARD',
        (4, 2, 3): 'RICHARD',
        (4, 2, 4): 'RICHARD',
        (4, 3, 3): 'RICHARD',
        (4, 3, 4): 'GABRIEL',
        (4, 4, 4): 'GABRIEL',
        }

def winner(X, R, C):
    if R > C:
        return winner_dic[X, C, R]
    else:
        return winner_dic[X, R, C]


T = int(raw_input())
for case_number in range(1, T + 1):
    X, R, C = map(int, raw_input().split())
    print 'Case #%d: %s' % (case_number, winner(X, R, C))
