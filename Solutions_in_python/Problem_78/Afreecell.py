#!/usr/bin/python3

from sys import argv
from math import floor

infile = open(argv[1])
t = int(infile.readline())
for i in range(t):
    n, pd, pg = map(int, infile.readline().split())
    possible = False
    for j in range(1, n+1):
        won = j * pd / 100
        if won == floor(won):
            possible = True
            games = j
            break
    if pg == 100 and pd < 100:
        possible = False
    if pg == 0 and pd > 0:
        possible = False
    possible2 = False
    if possible:
        for j in range(0, 10000000000):
            x = pg * (games + j) / 100
            if x == floor(x):
                possible2 = True
                # print('N={} PD={} PG={} Today {} All {}'.format(n, pd, pg, games, j))
                break
    possible = possible and possible2
    print('Case #{}: {}'.format(i+1, 'Possible' if possible else 'Broken'))
