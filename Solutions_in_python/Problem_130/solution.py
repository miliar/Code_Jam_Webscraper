# -*- coding: utf-8 -*-

import bisect


def worst_next_round(group_begin, group_size, number_of_winners):
    if number_of_winners == 0:
        return (group_begin, group_size / 2, 0)
    return (group_begin + group_size / 2, group_size / 2, (number_of_winners-1) / 2)

def worst_position(N, x):
    group_begin, group_size, number_of_winners = 0, 2**N, x
    while group_size > 1:
        group_begin, group_size, number_of_winners = worst_next_round(group_begin, group_size, number_of_winners)
    return group_begin


def best_next_round(group_begin, group_size, number_of_winners):
    if number_of_winners + 1 == group_size:
        return (group_begin + group_size / 2, group_size / 2, group_size/2 - 1)
    return (group_begin, group_size / 2, (number_of_winners+1) / 2)

def best_position(N, x):
    group_begin, group_size, number_of_winners = 0,2**N, x
    while group_size > 1:
        group_begin, group_size, number_of_winners = best_next_round(group_begin, group_size, number_of_winners)
    return group_begin



def bisect_left(predicate, first, last):
    while first < last:
        c = (first + last + 1) / 2
        if predicate(c):
            first = c
        else:
            last = c - 1
    return first


def solve(N, P):
    
    return (bisect_left(lambda x: worst_position(N, x) < P, 0, 2**N - 1),
            bisect_left(lambda x: best_position(N, x) < P, 0, 2**N - 1))



import sys

number_of_cases = int(sys.stdin.readline())
for case in xrange(1, number_of_cases + 1):
    N, P = map(int, sys.stdin.readline().split())
    print "Case #%d:" % case, "%d %d" % solve(N, P)
