#!/usr/bin/python

import os, sys, copy, time, itertools

def able_triplets(s):
    able_triplets = []
    upper_limit = min(10, s)
    for first in xrange(0, upper_limit + 1):
        lower_limit = max(0, s - first - 10)
        upper_limit = min(10, s - first)
        for second in xrange(lower_limit, upper_limit + 1):
            third = s - first - second
            if abs(first - second) > 2 or abs(second - third) > 2 or abs(first - third) > 2:
                continue
            if sum([first, second, third]) != s:
                continue
            able_triplets.append((first, second, third))
    return able_triplets

def count_surprise(triplets):
    num_of_surprise = 0
    for triplet in triplets:
        if abs(triplet[0]- triplet[1]) >= 2 or abs(triplet[1] - triplet[2]) >= 2 or abs(triplet[2] - triplet[0]) >= 2:
            num_of_surprise += 1
    return num_of_surprise

def count_goodies(triplets, lower_limit):
    return len([True for triplet in triplets if max(triplet) >= lower_limit])

def solve(line):
    global able_triplets
    values = line.split()

    number_of_googlers = int(values.pop(0))
    given_num_of_surprise = int(values.pop(0))
    lower_limit_of_best_result = int(values.pop(0))
    sums_of_triplets = map(int, values)

    num_of_good_result = 0
    best_goodies = 0

    triplets = [able_triplets(s) for s in sums_of_triplets]
    iter = itertools.product(*triplets)

    while True:
        try:
            triplets = iter.next()
            for expected, actual in zip(sums_of_triplets, triplets):
                if expected != sum(actual):
                    continue
            if count_surprise(triplets) != given_num_of_surprise:
                continue
            new_goodies = count_goodies(triplets, lower_limit_of_best_result)
            if new_goodies > best_goodies:
                best_goodies = new_goodies
        except StopIteration:
            break

    return best_goodies
    
lines = sys.stdin.read().split('\n')
lines.pop(0)
lines.pop()

case = 0
while lines:
    case += 1
    line = lines.pop(0)

    print 'Case #%d: %s' % (case, solve(line))
