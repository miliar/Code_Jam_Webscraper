#!/usr/bin/env python
# encoding: utf-8

import os

def parse_input(file_descriptor):
    f = file_descriptor
    # n = number of teams
    n = int(f.readline())
    sch = []
    for i in xrange(n):
        sch.append((f.readline()[:-1]))
    return sch

def wp(sch):
    result = []
    for team in sch:
        r = 0
        w = 0
        for match in team:
            if match != '.':
                r += 1
                w += int(match)
        result.append(float(w)/r)
    return result

def owp(sch):
    result = []
    for i in xrange(len(sch)):
        r = 0
        w = 0
        for j in xrange(len(sch[i])):
            if sch[i][j] != '.':
                r += 1
                w += single_owp(sch, j, i)
        result.append(float(w)/r)
    return result

def single_owp(sch, i, j):
    r = 0
    w = 0
    for x in xrange(len(sch[i])):
        if x != j and sch[i][x] != '.':
            r += 1
            w += int(sch[i][x])
    return (float(w)/r)

def oowp(sch, l_owp):
    result = []
    for i in xrange(len(sch)):
        r = 0
        w = 0
        for j in xrange(len(sch[i])):
            if sch[i][j] != '.':
                r += 1
                w += l_owp[j]
        result.append(float(w)/r)
    return result

def solve_case(sch):
    wp_l  = wp(sch)
    owp_l = owp(sch)
    oowp_l = oowp(sch, owp_l)

    result = []
    for i in xrange(len(sch)):
        rpi = 0.25 * wp_l[i] + 0.5 * owp_l[i] + 0.25 * oowp_l[i]
        result.append(rpi)
    return result

def solve(fileName):
    f = open(fileName, "r")
    fsol = open("solution.txt", "w")

    # Number of test cases
    test_cases = int(f.readline())

    for i in xrange(test_cases):
        args = parse_input(f)
        result = solve_case(args)
        fsol.write("Case #%d:\n" %(i+1))
        for sol in result:
            fsol.write(str(sol)+'\n')
