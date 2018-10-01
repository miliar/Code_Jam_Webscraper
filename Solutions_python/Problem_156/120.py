# -*- coding: utf-8 -*-
import sys
import math

def calc_minutes(diner_num, ini_state):
    best_sum = sum(ini_state) - len(ini_state) + 1
    dec_flag = False

    for separate_num in xrange(2, max(ini_state)+1):
        lam = lambda n:int(math.ceil(float(n)/separate_num))-1
        current_sum = sum(map(lam, ini_state)) + separate_num
        if best_sum > current_sum:
           best_sum = current_sum

    return best_sum

if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    test_num = int(f.readline())

    for i in xrange(1, test_num+1):
        diner_num = int(f.readline())
        def_state = map(int, f.readline().split())
        ans = calc_minutes(diner_num, def_state)
        print('Case #%i: %s' % (i, ans) )
