#!/usr/env/python
import math

def get_min_minutes(D, P):
    max_height = max(P)
    min_height = min(P)
    min_time = 999999999
    for ideal_ht in range(1, max_height + 1):
        t = 0
        for i in range(len(P)):
            if P[i] > ideal_ht:
                t += math.ceil((P[i] - ideal_ht) / float(ideal_ht))
        min_time = min(min_time, t + ideal_ht)
    return min_time

if __name__ == '__main__':
    T = int(raw_input())
    for t in range(1, T + 1):
        D = int(raw_input())
        P = map(int, raw_input().split())
        print 'Case #%d: %d' % (t, get_min_minutes(D, P))
