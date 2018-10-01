#! /usr/bin/env python
# -*- coding: utf-8 -*-
#

def StandingOvation(s_max, s):
    length = s_max + 1
    num = 0
    s_list = []
    lack_max = 0
    for i in range(length):
        s_list.append(num)
        lack = i - num
        if (lack > lack_max):
            lack_max = lack
        num += int(s[i])
    return lack_max

f_in = open('A-large.in', 'r')
f_out = open('A-large.out', 'w')
t_string = f_in.readline()
t = int(t_string.strip('\n'))
for i in range(t):
    case = f_in.readline().split()
    result = StandingOvation(int(case[0]), case[1])
    f_out.write('Case #' + str(i+1) + ': ' + str(result) + '\n')

f_in.close()
f_out.close()
