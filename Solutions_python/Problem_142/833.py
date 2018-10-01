#!/usr/bin/env python
#coding: UTF-8
'''
Solution for the Repeater problem of Google Code Jam 2014 Round B1

Copyright (c) 2014 Samuel Groß
'''

INPUTFILE  = "/home/sam/Desktop/small.in"
OUTPUTFILE = "/home/sam/Desktop/small.out"


# ------------------- #
#      Functions      #
# ------------------- #

def remove_dups(s):
    res = ""
    last = ""
    for c in s:
        if c != last:
            res += c
            last = c
    return res

def groups(w):
    res = []
    last = ""
    for c in w:
        if c == last:
            res[-1] += c
        else:
            res.append(c)
            last = c
    return res

def calc_ops(w1, w2):
    return sum([abs(len(x) - len(y)) for x, y in zip(groups(w1), groups(w2))])


def solve(strings):
    if all(x == strings[0] for x in strings):
        return 0

    minimum = remove_dups(strings[0])
    if not all(x == minimum for x in map(remove_dups, strings)):
        return "Fegla Won"

    additionals = [minimum]

    ops = []
    for string in strings + additionals:
        ops.append(0)
        for other in strings:
            ops[-1] += calc_ops(other, string)


    return min(ops)



if __name__ == '__main__':

    infile = open(INPUTFILE, 'r')
    outfile = open(OUTPUTFILE, 'w')

    testcases = int(infile.readline())
    counter = 1

    for i in range(testcases):
        nums = int(infile.readline())
        input = []
        for j in range(nums):
            input.append(infile.readline())

        sol = solve(input)	
        print("[*] Case %i solved, %.2f%% done" % (counter, float(counter) * 100 / testcases))
        outfile.write("Case #%i: %s\n" % (counter, sol))
        counter += 1
