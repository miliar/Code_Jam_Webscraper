#!/usr/bin/python
# vi: set fileencoding=utf-8 :

'''
Google code jam 2015 qualification round
B: Infinite House of Pancakes
'''

def smallest_minutes(pancake):
    if pancake[-1] <= 3:
        return pancake[-1]
    else: 
        minimum = pancake[-1]
        for i in range(2, pancake[-1] / 2 + 1):
            devide = pancake[-1] / i
            moved_pancake = pancake[:]
            moved_pancake.append(devide)
            moved_pancake[-2] -= devide
            moved_pancake.sort()
            minimum = min(minimum, 1 + smallest_minutes(moved_pancake))
        return minimum


T = int(raw_input())
for case_number in range(1, T + 1):
    D = int(raw_input())
    pancake = map(int, raw_input().split())
    pancake.sort()
    print 'Case #%d: %d' % (case_number, smallest_minutes(pancake))
