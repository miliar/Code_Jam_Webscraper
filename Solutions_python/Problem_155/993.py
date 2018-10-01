import sys
import collections
import math

def rl():
    return tuple(raw_input().strip().split())

def solve(max_s, people):
    #print '====== ' + str(locals())
    friends = 0
    people = map(int, people)
    for i in range(len(people)-1, 1, -1):
        lack = i - sum(people[:i])
        if lack > 0:
            people[0] += lack
            friends += lack
    if people[0] == 0:
        friends += 1
    return friends

if __name__ == '__main__':
    for case in range(int(raw_input())):
        print 'Case #%d: %d' % (case+1, solve(*rl()))