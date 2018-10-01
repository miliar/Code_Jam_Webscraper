#!/usr/bin/python

import sys, math

class Train:
    def __init__(self, available=0, location=0):
        self.available = available
        self.location=location
    def available(self, t):
        return self.available <= t
    def setAvailable(self, t):
        self.available = t
    def lt(self, other):
        return self.available < other.available
    def gt(self, other):
        return self.available > other.available

class Trip:
    def __init__(self, start=0, end=0, origin=0):
        self.start=start
        self.end=end
        self.origin = origin
    def start(self):
        return self.start
    def end(self):
        return self.end
    def lt(self, other):
        return self.start < other.start
    def gt(self, other):
        return self.start > other.start
    def __str__(self):
        return "%s %s -- Leaving %s" % (self.start,self.end,self.origin)


def trainTimetable(trips, turnaround):
    trains=[]
    trips.sort(lambda a,b:cmp(a.start,b.start))
    start={0:0,1:0}

    for trip in trips:
        trainsHere = [x for x in trains if x.location == trip.origin and x.available <= trip.start]
        if not(trainsHere):
            train=Train(0,trip.origin)
            trains.append(train)
            start[trip.origin] += 1
        else:
            train = trainsHere[0]
        train.location = 1 - trip.origin
        train.available = trip.end + turnaround
    keys = start.keys()
    keys.sort()
    return " ".join([str(start[k]) for k in keys])


if __name__=="__main__":
    fpin=open(sys.argv[1])
    if len(sys.argv) > 2:
        fpout = open(sys.argv[2], 'w')
    else:
        fpout = sys.stdout


    cases = int(fpin.readline().strip())
    for case in range(1,cases+1):
        trips=[]
        turnaround = float(fpin.readline().strip())
        (NA, NB) = [int(x) for x in fpin.readline().strip().split()]
        for a in range(NA):
            (start,end) = fpin.readline().strip().split()
            (min,sec) = start.split(":")
            start = int(min) * 60 + int(sec)
            (min,sec) = end.split(":")
            end = int(min) * 60 + int(sec)
            trips.append(Trip(start,end,0))
        for b in range(NB):
            (start,end) = fpin.readline().strip().split()
            (min,sec) = start.split(":")
            start = int(min) * 60 + int(sec)
            (min,sec) = end.split(":")
            end = int(min) * 60 + int(sec)
            trips.append(Trip(start,end,1))
        fpout.write("Case #%d: %s\n" % (case, trainTimetable(trips, turnaround)))

