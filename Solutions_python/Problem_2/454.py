#! /usr/bin/python
"""
Google code jam 2008
  Qualification Round
  B. Train Timetable

Ramsey Nasser
  http://ramseynasser.com/
  ramsey@ramseynasser.com

Initially, one train is assigned to each scheduled trip. This is the maximum
possible number of trains. Then, in order to reuse the trains, they are 
"matched" to trips leaving after their turnaround time.
"""

import sys

def stamp(timestr):
    """Convert a time string (str) into a stamp (int).
    
    The stamp is the number of minutes since 0:00
    
    eg:
    12:00 => 720
    01:00 => 75
    23:59 => 1439
    """
    h, m = timestr.split(":")
    return 60 * int(h) + int(m)

inlist = [line.strip() for line in open(sys.argv[1])]
N = int(inlist.pop(0))
# Handle a test case
for i in range(N):
    T = int(inlist.pop(0))
    NA, NB = [int(n) for n in inlist.pop(0).split()]
    
    # Initially, the number of trains is NA, NB. Work down from there 
    ta, tb = NA, NB
    
    # Populate A's schedule
    A = []
    for j in range(NA):
        dep, arr = [stamp(t) for t in inlist.pop(0).split()]
        A.append((dep, arr))
    # Sort by departure time
    A.sort(lambda x, y: x[0] - y[0])
    
    # Populate B's schedule    
    B = []
    for j in range(NB):
        dep, arr = [stamp(t) for t in inlist.pop(0).split()]
        B.append((dep, arr))
    # Sort by departure time
    B.sort(lambda x, y: x[0] - y[0])
    
    matched = []
    
    # Trains arriving at B then departing to A
    for trip_a in A:
        for trip_b in B:
            dep = trip_b[0]
            arr = trip_a[1]
            
            if dep >= (arr + T) and trip_b not in matched:
                tb -= 1
                matched.append(trip_b)
                break
        
    # Trains arriving at A then departing to B
    for trip_b in B:
        for trip_a in A:
            dep = trip_a[0]
            arr = trip_b[1]
            
            if dep >= (arr + T) and trip_a not in matched:
                ta -= 1
                matched.append(trip_a)
                break
    
    print "Case #%d: %d %d"%(i+1, ta, tb)