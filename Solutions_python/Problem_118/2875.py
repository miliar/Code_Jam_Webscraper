#!/usr/bin/env python
import sys
from math import log10

def is_palindromes(num):
    num = str(num)
    strlen = len(num)
    for i in range(int(strlen/2)):
        if num[i] != num[strlen-1-i]:
            return 0
    return 1



def is_square(num):
    if int(num**0.5)**2 == num:
        return 1
    else:
        return 0

def check_fair_sq(num):
    if is_palindromes(num):
        num_sq = num ** 2
        if is_palindromes(num_sq) == 1:
            return 1
    return 0


def check(lb, ub):
    sq_lb = int(lb**0.5 + 0.0001)
    if sq_lb**2 < lb:
        sq_lb += 1
    sq_ub = int(ub**0.5 + 0.0001)
    res = 0
    #print 'range', sq_lb, sq_ub
    p_lb = int(  (log10(sq_lb) + 0.001) )
    p_ub = int(  (log10(sq_ub) + 0.001) + 1)
    #print 'p', p_lb, p_ub
    for num_len in range(p_lb, p_ub+1):
        #print 'now',num_len
        if num_len == 0:
            continue
        elif num_len == 1:
            for num in range(10):
                if num >= sq_lb and num <= sq_ub:
                    res += check_fair_sq(num)
        elif num_len % 2 == 0:
            for i in range(10 ** int(num_len/2-1), 10 ** int(num_len/2) ):
                num = int(str(i) + str(i)[::-1])
                #print 's',sq_lb,num,sq_ub
                if num >= sq_lb and num <= sq_ub:
                    res += check_fair_sq(num)
        else:
            for i in range(10 ** max([int(num_len/2-1), 0]), 10 ** int(num_len/2)):
                for j in range(10):
                    num = int(str(i) + str(j) + str(i)[::-1])
                    if num >= sq_lb and num <= sq_ub:
                        res += check_fair_sq(num)
                        #print 'found: ', num

#    for i in range(sq_lb, sq_ub+1):
#        if is_palindromes(i):
#            num_sq = i ** 2
#            if is_palindromes(num_sq) == 1:
#                res += 1
                #print 'found: ', num
    return res

def main():
    T = int(sys.stdin.readline().strip())
    for i in range(1, T+1):
        line = sys.stdin.readline().strip()
        spline = map(int, line.split(' '))
        print 'Case #%d: %d' % (i, check(spline[0], spline[1]))

main()
