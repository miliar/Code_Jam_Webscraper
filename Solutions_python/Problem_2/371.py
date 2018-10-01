#!/usr/bin/env python
# encoding: utf-8
"""
train.py

Created by Devin Naquin on 2008-07-16.
Copyright (c) 2008. All rights reserved.
"""

import sys

def main():
    num_tests = int(sys.stdin.readline().strip())
    assert(1 <= num_tests and num_tests <= 100)
    
    for i in range(num_tests):
        # Input
        turnaround = int(sys.stdin.readline().strip())
        num_a, num_b = map(int, sys.stdin.readline().strip().split(' '))
        assert(0 <= turnaround and turnaround <= 60)
        assert(0 <= num_a and num_a <= 100)
        assert(0 <= num_b and num_b <= 100)
        
        departs_from_a = []
        arrives_at_b = []
        for j in range(num_a):
            depart, arrive = sys.stdin.readline().strip().split(' ')
            depart_hour, depart_minute = map(int, depart.split(':'))
            arrive_hour, arrive_minute = map(int, arrive.split(':'))
            
            departs_from_a.append((depart_hour, depart_minute))
            if arrive_minute + turnaround > 60:
                arrive_hour += 1
                arrive_minute = arrive_minute + turnaround - 60
            else:
                arrive_minute += turnaround
            arrives_at_b.append((arrive_hour, arrive_minute))
        departs_from_a.sort()
        arrives_at_b.sort()

        departs_from_b = []
        arrives_at_a = []
        for j in range(num_b):
            depart, arrive = sys.stdin.readline().strip().split(' ')
            depart_hour, depart_minute = map(int, depart.split(':'))
            arrive_hour, arrive_minute = map(int, arrive.split(':'))
            
            departs_from_b.append((depart_hour, depart_minute))
            if arrive_minute + turnaround > 60:
                arrive_hour += 1
                arrive_minute = arrive_minute + turnaround - 60
            else:
                arrive_minute += turnaround
            arrives_at_a.append((arrive_hour, arrive_minute))
        departs_from_b.sort()
        arrives_at_a.sort()
        
        # Calculate
        start_a = 0
        for departure in departs_from_a:
            found = False
            for j, arrival in enumerate(arrives_at_a):
                if arrival<=departure:
                    del arrives_at_a[j]
                    found = True
                    break
                else:
                    break
            if not found:
                start_a += 1
        start_b = 0
        for departure in departs_from_b:
            found = False
            for j, arrival in enumerate(arrives_at_b):
                if arrival<=departure:
                    del arrives_at_b[j]
                    found = True
                    break
                else:
                    break
            if not found:
                start_b += 1
         
        print 'Case #%s: %s %s' % (i+1, start_a, start_b)

if __name__ == '__main__':
    main()
