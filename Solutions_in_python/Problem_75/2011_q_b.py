#!/usr/bin/env python
# -*- coding=utf-8 -*-

import sys



def main():
    # get num of cases
    n = int(sys.stdin.readline())
    for case in range(n):
        process(case)
        
def clearlist(stack):
    l = len(stack)
    for i in range(l):
        stack.pop()

def combine(stack, comrule, c):
    if len(stack) == 0:
        return False

    for rule in comrule:
        if stack[-1] in rule[0:2] and c in rule[0:2]:
            if stack[-1] != c or rule[0] == rule[1]:
                stack.pop()
                stack.append(rule[2])
                return True

    return False

def delete(stack, delrule, c):
    if len(stack) == 0:
        return False

    astack = stack + [c]
    for rule in delrule:
        if rule[0] in astack and rule[1] in astack:
            clearlist(stack)
            return True
    
    return False

def process(case):
    line = sys.stdin.readline().split()
    
    C = int(line.pop(0))
    comrule = []
    for i in range(C):
       comrule.append(line.pop(0))

    D = int(line.pop(0))
    delrule = []
    for i in range(D):
        delrule.append(line.pop(0))

    N = int(line.pop(0))
    seq = line.pop(0)

    #print comrule,delrule,seq

    stack = []
    for c in seq:
        if combine(stack, comrule, c):
            pass
        else:
            if delete(stack, delrule, c):
                pass
            else:
                stack.append(c)

    #print stack
    
    # print result
    res = '['
    for i in range(len(stack)):
        res += stack[i]
        if i != len(stack)-1:
            res += ", "
    res += "]"
    print("Case #{0}: {1}".format(case+1, res))



main()
