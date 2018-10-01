#!/usr/bin/env python

import sys

sys.setrecursionlimit(1500)

class tsched(object):
    def __init__(self,s_time=0,s_end=0,to=''):        
        self.s_time = s_time
        self.s_end = s_end
        self.to = to


def get_num_trains(sched):
    num_trains = 0
    t  = [0,0]
    lista = []
    listb = []
    if len(sched) == 0:
        return t
    if sched[0].to == 'b':
        t[0] = t[0] + 1
        lista.append(sched[0].s_end)
    else:
        t[1] = t[1] + 1
        listb.append(sched[0].s_end)
    for i in range(1,len(sched)):
        if sched[i].to == 'b':
            #Are there available trains to b?
            if (len(listb) > 0):
                if sched[i].s_time >= listb[0]:
                    listb.pop(0)
                    lista.append(sched[i].s_end)
                    lista.sort()
                else:
                    #No train is available
                    
                    t[0] = t[0] + 1
                    lista.append(sched[i].s_end)
                    lista.sort()
                    #print "I need a train: %d" % t[0]
                    #print sched[i].s_time
                    #print listb
            else:
               #No train is available
               t[0] = t[0] + 1
               lista.append(sched[i].s_end)
               lista.sort()
               #print "I need a train: %d" % t[0]
               #print sched[i].s_time
               #print listb        
        else:
            #Are there available trains to a?
            if (len(lista) > 0):
                if sched[i].s_time >= lista[0]:
                    lista.pop(0)
                    listb.append(sched[i].s_end)
                    listb.sort()
                else:
                    #No train is available
                    t[1] = t[1] + 1
                    listb.append(sched[i].s_end)
                    listb.sort()
            else:
                #No train is available
                t[1] = t[1] + 1
                listb.append(sched[i].s_end)
                listb.sort()    
                
    return t

def M_sort(a_start,a_end,b_start,b_end):
    t_a_start = []
    t_a_end = []
    t_b_start = []
    t_b_end = []
    sched = []
    # Sort a
    l = len(a_start)
    for i in range(l):
        ind = a_start.index(min(a_start))
        t_a_start.append(a_start.pop(ind))
        t_a_end.append(a_end.pop(ind))
    # Sort b
    m = len(b_start)
    for j in range(m):
        ind = b_start.index(min(b_start))
        t_b_start.append(b_start.pop(ind))
        t_b_end.append(b_end.pop(ind))
    
    i,j = 0,0
    while i < l and j < m:
        if t_a_start[i] < t_b_start[j]:
            #isc = tsched(t_a_start[i], t_a_end[i],'b')
            #isc.s_time = t_a_start[i]
            #isc.s_end = t_a_end[i]
            #isc.to = 'b'
            sched.append(tsched(t_a_start[i], t_a_end[i],'b'))
            i = i + 1
            
        else:
            isc = tsched(t_b_start[j],t_b_end[j], 'a')
            #isc.s_time = t_b_start[j]
            #isc.s_end = t_b_end[j]
            #isc.to = 'a'
            sched.append(isc)
            j = j + 1
            
            
    if i < l:
        while i < l:
            sched.append(tsched(t_a_start[i], t_a_end[i],'b'))
            i = i + 1
    
    if j < m:
        while j < m:
            isc = tsched(t_b_start[j],t_b_end[j], 'a')
            sched.append(isc)
            j = j + 1
                
    return sched

def main():
    
    f = file("B-large.in", "r")
    of = file("output.out", "w")
    
    num_cases = f.readline()

    for i in range(int(num_cases)):
        a_start = []
        a_end = []
        b_start = []
        b_end = []
        turnaround = int(f.readline())
        trip_str = f.readline()
        ab_trips = int(trip_str.split(' ')[0])
        ba_trips = int(trip_str.split(' ')[1])
        for j in range (ab_trips):
            time_str = f.readline()
            temp_a_start = time_str.split(' ')[0]
            temp_a_end = time_str.split(' ')[1]
            thr = int(temp_a_start.split(':')[0])
            tmin = int (temp_a_start.split(':')[1])
            a_start.append((thr * 60) + tmin)
            thr = int(temp_a_end.split(':')[0])
            tmin = int (temp_a_end.split(':')[1])
            a_end.append((thr * 60) + tmin + turnaround)
        for k in range (ba_trips):
            time_str = f.readline()
            temp_b_start = time_str.split(' ')[0]
            temp_b_end = time_str.split(' ')[1]
            thr = int(temp_b_start.split(':')[0])
            tmin = int (temp_b_start.split(':')[1])
            b_start.append(thr * 60 + tmin)
            thr = int(temp_b_end.split(':')[0])
            tmin = int (temp_b_end.split(':')[1])
            b_end.append(thr * 60 + tmin + turnaround)
        
        sched = M_sort(a_start,a_end,b_start,b_end)
        #for s in sched:
        #    print s.s_time, s.s_end, s.to
        #print "***********"
        t = get_num_trains(sched)  
        #print t  
        
        
        of.write("Case #%d: %d %d\n" % ((i+1),t[0],t[1]))
        print "Case #%d: %d %d" % ((i+1),t[0], t[1])
        