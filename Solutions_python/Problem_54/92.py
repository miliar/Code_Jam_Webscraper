#!/usr/bin/env python

import sys

def differences(list):
    result = []
    while len(list) > 0:
        head = list[0]
        tail = list[1:]
        result.extend([abs(head - x) for x in tail])
        list = tail
    
    return result

def gcd(a, b):
    while True:
        if b == 0:
            return a
        
        temp = a % b
        if temp == 0:
            return b
        
        a = b
        b = temp

def main():
    nCases = int(sys.stdin.readline())
    case = 0

    for line in sys.stdin.readlines():
        case += 1
        if case > nCases:
            break;

        times = [int(x) for x in line.split(' ')][1:]
        durations = differences(times)
        goal = reduce(gcd, durations)
        apocalypse = goal - (times[0] % goal)
        if apocalypse == goal:
            apocalypse = 0
        
        print 'Case #%d: %d' % (case, apocalypse)

    
main()
