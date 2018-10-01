#!/usr/bin/python

import sys


def num_friends(members):
    friends = 0
    shyness = 0
    N_standing = 0
    for m in members:
        if shyness <= N_standing:
            N_standing += m
        else:
            friends += shyness - N_standing
            N_standing += m + (shyness - N_standing)
        shyness += 1
    return friends




f = open(sys.argv[1], 'r')

lines = f.readlines()
f.close()
#print "Lines:"
#print lines

for i in range(int(lines[0])):
    #friends = 0
    Smax, members = lines[i+1].split()
    Smax = int(Smax)
    members = map(int, list(members))
    friends = num_friends(members)
    print "Case #{:}: {:}".format(i+1, friends)

