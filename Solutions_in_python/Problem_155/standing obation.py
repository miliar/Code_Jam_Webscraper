__author__ = 'sanjay'
import sys

def find_friends(s, aud):
    sum = int(aud[0])
    friend = 0
    for i in range(1, len(aud)):
        if i > sum:
            friend += 1
            sum += 1 + int(aud[i])
        else:
            sum += int(aud[i])
    return friend
test = int(input())

for i in range(test):

    s, aud = map(str, sys.stdin.readline().split())

    print 'Case #%d: %d' % (i + 1, find_friends(int(s), aud))