# encoding=utf8
import math
import numpy as np
import itertools
# odd = (8*r**3 - 2*r)/6.0
# even = (4*r*(r+1)*(2*r+1))/6.0

if __name__ == '__main__':
    num_cases = int(raw_input())
    for case_num in xrange(num_cases):
        rad, vol = map(int, raw_input().split())
        count = 0
        while vol > 0:
            vol -= (rad+1)**2 - rad**2
            count += 1
            rad += 2
        if vol < 0:
            count -= 1
        print 'Case #%d: %s' % (case_num+1, count)
