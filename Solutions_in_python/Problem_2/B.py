#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Nycholas de Oliveira e Oliveira <nycholas@gmail.com>

def format_time(str_time):
    (minute, second) = [int(x) for x in str(str_time).split(":")]
    time = (minute * 3600) + (second * 60)
    return time
    
def plus_turnaround(lst_time, time_turnaround):
    for time in lst_time:
        time[1] += time_turnaround
    return lst_time
       
def first_time(lst_time):
    min_time = []
    if len(lst_time) > 0:
        min_time = lst_time[0]
        for time in lst_time:
            if min_time[0] > time[0]:
                min_time = time
    return min_time
    
def next_time(lst_time, last_time):
    min_time = []
    if len(lst_time) > 0:
        curr = last_time[2] == 'a' and 'b' or 'a'
        for time in lst_time:
            if time[0] >= last_time[1] and \
               (not min_time or (time[0] < min_time[0])) and \
               time[2] == curr:
                min_time = time
    return min_time
    
def del_time(lst_time, time_del):
    if len(time_del) == 0:
        return lst_time
    new_time = []
    for time in lst_time:
        if time_del[0] == time[0] and time_del[1] == time[1] and time_del[2] == time[2]:
            pass
        else:
            new_time.append(time)
    return new_time
    
nro_case = int(raw_input())
for case in range(nro_case):
    time_turnaround = int(raw_input()) * 60
    (nro_a, nro_b) = [int(x) for x in str(raw_input()).split(" ")]    
    hour_a = []
    for a in range(nro_a):
        hour_a.append([format_time(x) for x in str(raw_input()).split(" ")])
    hour_a = [x + ['a'] for x in plus_turnaround(hour_a, time_turnaround)]
    hour_b = []
    for b in range(nro_b):
        hour_b.append([format_time(x) for x in str(raw_input()).split(" ")])
    hour_b = [x + ['b'] for x in plus_turnaround(hour_b, time_turnaround)]   
    hours = hour_a + hour_b    
    a = 0
    b = 0
    while hours:
        curr_time = first_time(hours)
        hours = del_time(hours, curr_time)
        if curr_time[2] == 'a': 
            a += 1
        else:
            b += 1
        curr_time = next_time(hours, curr_time)
        hours = del_time(hours, curr_time)
        while curr_time:
            curr_time = next_time(hours, curr_time)
            hours = del_time(hours, curr_time)
    print "Case #%d: %d %d" % (case + 1, a, b)
