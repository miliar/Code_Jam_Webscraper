#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Problem

Alice and Bob have a lawn in front of their house, shaped as a rectangle of N by M metres. Each year, they try to cut the lawn in some interesting pattern. So far, they had to do it with shears, which was very time-consuming, but now they have a new automatic lawnmower with multiple settings, and they want to try it out.

The new lawnmower has a height setting - you can set it to any height h between 1 and 100 millimetres, and it will cut all the grass higher than h it encounters to height h. You run it by entering the lawn at any part of the edge of the lawn, and the lawnmower goes in a straight line, perpendicular to the edge of the lawn it entered, cutting grass in a swath 1m wide, until it exits the lawn on the other side.

Alice and Bob have a number of various patterns of grass that they could have on their lawn. For each of those, they want to know whether it's possible to cut the grass into this pattern with their new lawnmower. Each pattern is described by specifying the height of the grass on each 1m x 1m square of the lawn.

The grass is 100mm high on the whole lawn initially.

Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing two numbers: N and M. Next follow N lines, with the ith line containing M numbers ai,j each, the number ai,j describing the desired height of the grass in the jth square of the ith row.

Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is either the word "YES" if it's possible to get the x-th pattern using the lawnmower, or "NO", if it's impossible (quotes for clarity only).

Limits

1 ≤ T ≤ 100.

Small dataset

1 ≤ N, M ≤ 10.
1 ≤ ai,j ≤ 2.
Large dataset

1 ≤ N, M ≤ 100.
1 ≤ ai,j ≤ 100.
Sample


Input
     
3
3 3
2 1 2
1 1 1
2 1 2
5 5
2 2 2 2 2
2 1 1 1 2
2 1 2 1 2
2 1 1 1 2
2 2 2 2 2
1 3
1 2 1

Output 

Case #1: YES
Case #2: NO
Case #3: YES

"""
import sys

FILL = 999

def ans(N, M, pattern):
    min_a = min([min(pat) for pat in pattern]) 
    max_b = max([max(pat) for pat in pattern])

    for search in range(min_a, max_b):
        for y in range(N):
            if pattern[y][0] == search:
                a = set(pattern[y])
                if a in [set([search])]:
                    for x in range(M):
                        pattern[y][x] = FILL
        for x in range(M):
            if pattern[0][x] == search or pattern[0][x] == FILL:
                a = set([pat[x] for pat in pattern])
                if a in [set([search]), set([search,FILL])]:
                    for y in range(N):
                        pattern[y][x] = FILL

    if min([min(pat) for pat in pattern]) != max_b:
        return 'NO'
    else:
        return 'YES'


with open(sys.argv[1]) as fr, open('b.out', 'w') as fw:
    T = int(fr.readline())
    for i in range(T):
        no = i + 1
        (N, M) = map(int, fr.readline().split(' '))
        pattern = [ map(int, fr.readline().split(' ')) for _ in range(N)]
        fw.write("Case #{no}: {ans}\n".format(no=no,ans=ans(N, M, pattern)))



# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
