#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Google CodeJam
Qualification Round
Task B - Train Timetable

Solution by Joao Moreno <alph.pt@gmail.com> 2008

Usage: python [source_file] < [input_file] > [output_file]
"""

import datetime as dt

class Trip(object):
    def __init__(self, trip, origin, destination):
        [self.departure, self.arrival] = [dt.datetime.strptime(i,"%H:%M") for i in trip.split()]
        self.origin = origin
        self.destination = destination
    
    def __cmp__(self, other):
        return cmp(self.departure, other.departure)
    
    def __repr__(self):
        return "%i:%i" % (self.d.hour, self.d.minute)

class TrainStation(object):
    def __init__(self, turnaround, trips):
        self.t = dt.timedelta(minutes=turnaround)
        self.schedule = sorted(trips)
    
    def minTrains(self):
        trains = [[],[]]
        minTrains = [0,0]
        for a in self.schedule:
            if len(trains[a.origin]) == 0 or a.departure < trains[a.origin][0]:
                minTrains[a.origin] += 1
            else:
                del trains[a.origin][0]
            trains[a.destination].append(a.arrival + self.t)
            trains[a.destination].sort()
        return tuple(minTrains)

if __name__ == '__main__':
    from codejam.io import Scanner
    s = Scanner()
    N = s.readInt()
    for i in range(1,N+1):
        T = s.readInt()
        NA = s.readInt()
        NB = s.readInt()
        A = [Trip(s.readLine(), 0, 1) for a in range(NA)]
        B = [Trip(s.readLine(), 1, 0) for b in range(NB)]
        r = TrainStation(T, A + B).minTrains()
        print "Case #%i: %i %i" % (i, r[0], r[1])
        
