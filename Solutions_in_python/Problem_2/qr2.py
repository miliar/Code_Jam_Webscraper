#!/usr/bin/env python

import sys

testcases = int(sys.stdin.readline())
for t in range(1, testcases + 1):
    turnaroundtime = int(sys.stdin.readline())
    timetable = {'a2b': {'starttime':[], 'endtime': []}, 'b2a': {'starttime': [], 'endtime': []}}
    na, nb = map(lambda x: int(x), sys.stdin.readline().split())
    while na > 0:
        train = [int(i[0])*60 + int(i[1]) for i in map(lambda x: x.split(':'), sys.stdin.readline().split())]
        timetable['a2b']['starttime'].append(train[0])
        timetable['a2b']['endtime'].append(train[1])
        na -= 1
    while nb > 0:
        train = [int(i[0])*60 + int(i[1]) for i in map(lambda x: x.split(':'), sys.stdin.readline().split())]
        timetable['b2a']['starttime'].append(train[0])
        timetable['b2a']['endtime'].append(train[1])
        nb -= 1
    train = {'a2b': [], 'b2a': []}
    starttrain = {'a2b': 0, 'b2a': 0}
    for time in range(0, 24*60):
        for i in range(0, timetable['a2b']['endtime'].count(time - turnaroundtime)):
            train['a2b'].remove(1)
            train['b2a'].append(0)
        for i in range(0, timetable['b2a']['endtime'].count(time - turnaroundtime)):
            train['b2a'].remove(1)
            train['a2b'].append(0)
        for i in range(0, timetable['a2b']['starttime'].count(time)):
            if 0 not in train['a2b']:
                train['a2b'].append(1)
                starttrain['a2b'] += 1
            else:
                train['a2b'][train['a2b'].index(0)] = 1
        for i in range(0, timetable['b2a']['starttime'].count(time)):
            if 0 not in train['b2a']:
                train['b2a'].append(1)
                starttrain['b2a'] += 1
            else:
                train['b2a'][train['b2a'].index(0)] = 1
    print 'Case #%d: %d %d' % (t, starttrain['a2b'], starttrain['b2a'])
