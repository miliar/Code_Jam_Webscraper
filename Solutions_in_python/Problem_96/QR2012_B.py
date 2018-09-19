# -*- coding: utf-8 -*-

# QUALIFICATION ROUND 2012 - PROBLEM B
# Author: Paul Mollet-Padier

def QR2012_B():
    def pp(t, p, s):
        if 3*p-t <= 2+2*s and t-p >= 0:
            return True
        else:
            return False
    
    f = open('B-large.in')
    o = open('B-large.out', 'w')
    
    T = int(f.readline())

    for i in range(T):
        nums = f.readline().split(' ')
        N = int(nums[0])
        S = int(nums[1])
        p = int(nums[2])
        t = nums[3:]
        g = 0
        for j in range(N):
            if pp(int(t[j]), p, 0):
                g += 1
            elif S > 0 and pp(int(t[j]), p, 1):
                g += 1
                S -= 1
        o.write('Case #' + str(i+1) + ': ' + str(g) + '\n')
