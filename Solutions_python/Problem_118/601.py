# -*- coding: utf-8 -*-


import math
from itertools import permutations


def gen_palindromic(start, end):

    (str_start, str_end) = (str(start), str(end))
    result = []
    if len(str_start) == 1:
        for i in xrange(1, 10):
            result.append(i)
        str_start += '0'
    for p in xrange(len(str_start), len(str_end)+1):
        for i in xrange(pow(10, int(math.floor(p/2))-1), pow(10, int(math.ceil(p/2)))):
            str_i = str(i)
            if p%2 == 0:
                result.append(int(str_i+str_i[::-1]))
            else:
                for j in xrange(0, 10):
                    result.append(int(str_i+str(j)+str_i[::-1]))
    return result

def is_palindromic(nb):
    nb = str(nb)
    i = 0
    while i < len(nb):
        if nb[i] != nb[len(nb) - (i+1)]:
            return False
        i += 1
    return True


n = int(input())
interval_set = []
for i in xrange (0, n):
    interval = raw_input().split(' ')
    interval_set.append([int(nb) for nb in interval])

i = 1
for interval in interval_set:
    n = 0
    palindromic_set =  gen_palindromic(int(math.sqrt(interval[0])), int(math.sqrt(interval[1])))
    for palindromic in palindromic_set:
        pow_palindromic = pow(palindromic, 2)
        if is_palindromic(pow_palindromic) and interval[0] <= pow_palindromic and interval[1] >= pow_palindromic:
            n += 1
    print "Case #"+str(i)+": "+str(n)
    i += 1

