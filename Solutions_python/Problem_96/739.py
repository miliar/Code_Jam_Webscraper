#!/usr/bin/env python

import sys

def iterate_input():
    t = int(sys.stdin.readline())
    for i in range(t):
        line = sys.stdin.readline().split(' ')
        n, s, p = map(int, line[0:3])
        total_points = map(int, line[3:3+n])
        yield i+1, s, p, total_points

def all_combinations():
    combinations = [{}]*31
    for i in range(31):
        combinations[i] = get_combinations(i)
#        print "%d: %s, %s" % (i, 
#                              combinations[i].get('normal'), 
#                              combinations[i].get('surprising'))
    return combinations

def is_acceptable(i, j, k):
    return abs(i-j) <= 2 and abs(i-k) <= 2 and abs(j-k) <= 2

def is_normal(i, j, k):
    return is_acceptable(i, j, k) and not is_surprising(i, j, k)

def is_surprising(i, j, k):
    return is_acceptable(i, j, k) and (abs(i-j) == 2 or abs(i-k) == 2 or abs(j-k) == 2)

def get_combinations(total_points):
    s = set()
    for i in range(11):
        for j in range(11):
            for k in range(11):
                if sum([i, j, k]) == total_points and is_acceptable(i, j, k):
                    s.add(tuple(sorted([i, j, k])))
    result = {'count': len(s)}
    for combination in s:
        if is_normal(*combination):
            result['normal'] = combination
            result['normal_best'] = max(combination)
        elif is_surprising(*combination):
            result['surprising'] = combination
            result['surprising_best'] = max(combination)
    return result

def better_surprising(i, p, combinations):
    if (combinations[i].get('surprising_best', -1) == p and
        combinations[i].get('normal_best', -1) == p-1):
        return i+100
    else:
        return i
        
c = all_combinations()

for case_no, surprises, p, total_points in iterate_input():
    #print "Case #%d: S=%d, P=%d; %s" % (case_no, surprises, p, total_points)
    count_good = 0
    count_surprises = 0
    sorted_points = sorted(total_points, key=lambda i: better_surprising(i, p, c), reverse=True)
    #print sorted_points
    for points in sorted_points:
        #print "checking %d %s points total (%d surprises)" % (points, c[points], count_surprises)
        if (c[points].has_key('surprising_best') and count_surprises < surprises):
            count_surprises += 1
            #print "surprising_best %d" % c[points]['surprising_best']
            if c[points]['surprising_best'] >= p:
                #print "found %s" % (c[points]['surprising'],)
                count_good += 1
        elif c[points]['normal_best'] >= p:
            #print "found %s" % (c[points]['normal'],)
            count_good += 1
    print "Case #%d: %d" % (case_no, count_good)
    if count_surprises < surprises:
        print "WTF ?!! I didn't find enough surprises"
        

