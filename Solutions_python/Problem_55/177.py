#!/usr/bin/python

T = int(raw_input())

for i in range(T):
    R, k, N = (int(v) for v in raw_input().split(' '))
    Gs = [int(v) for v in raw_input().split(' ')]

    euros = 0
    frontGroup = 0
    for j in range(R):
        passengers = 0
        groupCount = 0
        while groupCount < N:
            nextGroup = Gs[(frontGroup + groupCount) % N]
            if (passengers + nextGroup > k):
                break
            passengers += nextGroup
            groupCount += 1
        frontGroup = (frontGroup + groupCount) % N
        euros += passengers
    print("Case #%d: %s" % (i + 1, euros))
    
