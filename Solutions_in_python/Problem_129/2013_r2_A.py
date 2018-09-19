'''
CodeJam Practice 
Created on 2013-06-01

@author: festony
'''

from cj_lib import *
from properties import *

#curr_file_name = 'A-large'
curr_file_name = 'A-small-attempt1'
#curr_file_name = 'test'

# map(int, input_lines.pop(0).split(' '))

def input_dividing_func(input_lines):
    total_case = int(input_lines.pop(0))
    case_inputs = []
    for i in range(total_case):
        N, M = map(int, input_lines.pop(0).split(' '))
        P = []
        for j in range(M):
            P.append(map(int, input_lines.pop(0).split(' ')))
        case_inputs.append([N, M, P])
    return case_inputs

def calc_ori(N, P):
    total_inc = 0
    for p in P:
        x = p[1]-p[0]
        single =  N * x - x*(x-1)/2
        total_inc += single * p[2]
    return total_inc

def proc_station(N, o, e):
    inc = 0
    if o == [] or e == []:
        return inc
    last_e = e[-1]
    first_o = o[0]
    p = min(last_e[1], first_o[1])
    x = last_e[0] - first_o[0]
    single = N * x - x*(x-1)/2
    inc = single * p
    last_e[1] -= p
    first_o[1] -= p
    if last_e[1] == 0:
        e.pop(-1)
    if first_o[1] == 0:
        o.pop(0)
    return inc

def proc_stat(N, traf):
    inc = 0
    if traf == []:
        return [inc, [[]]]
    print traf
    p = min(map(lambda x:x[2], traf[:-1]))
    p = min(p, traf[0][1], -traf[-1][1])
    print p
    x = traf[-1][0] - traf[0][0]
    #print x
    single = N * x - x*(x-1)/2
    #print single
    inc = single * p
    traf[0][1] -= p
    traf[-1][1] += p
    if traf != [] and traf[0][1] == 0:
        traf.pop(0)
    if traf != [] and traf[-1][1] == 0:
        traf.pop(-1)
    total = 0
    a_r_t = []
    r_t = []
    for t in traf:
        total += t[1]
        t[2] = total
        r_t.append(t)
        if total == 0:
            a_r_t.append(r_t)
            r_t = []
    #print traf
    #print '-----'
    #print traf
#    if traf == []:
#        return [inc, []]
    #print traf
#    for i, t in enumerate(traf):
#        if t[2] == 0:
#            if r_t != []:
#                a_r_t.append(r_t)
#                r_t = []
#            continue
#        r_t.append(t)
#    #print '---------'
#    if r_t != []:
#        a_r_t.append(r_t)
    return [inc, a_r_t]
    

    
def process_func(func_input):
    N, M, P = func_input
    ori_inc = calc_ori(N, P)
    #print N
    print ori_inc
    merged = {}
    for p in P:
        if merged.has_key(p[0]):
            merged[p[0]] += p[2]
        else:
            merged[p[0]] = p[2]
        if merged.has_key(p[1]):
            merged[p[1]] -= p[2]
        else:
            merged[p[1]] = -p[2]
    all_traf = []
    total = 0
    traf = []
    for k in sorted(merged.keys()):
        if merged[k] != 0:
            total += merged[k]
            traf.append([k, merged[k], total])
            if total == 0:
                all_traf.append(traf)
                traf = []
    merged_inc = 0
    print '--', all_traf
#    for traf in all_traf:
#        o = []
#        e = []
#        for s in traf:
#            if s[1] > 0:
#                o.append([s[0], s[1]])
#            if s[1] < 0:
#                e.append([s[0], -s[1]])
#        print o, e
#        inc = proc_station(N, o, e)
#        while e != [] and o != []:
#            print o, e, inc
#            merged_inc += inc
#            inc = proc_station(N, o, e)
#        merged_inc += inc
    while all_traf != []:
        t = all_traf.pop(0)
        inc, t = proc_stat(N, t)
        merged_inc += inc
        if t != []:
            all_traf += t
    return ori_inc - merged_inc

run_proc(process_func, input_dividing_func, curr_working_folder, curr_file_name)

#N = 10
#traf = [[1, 3, 3], [3, 1, 4], [4, -2, 2], [7, 2, 4], [9, -4, 0]]
#print proc_stat(N, traf)


