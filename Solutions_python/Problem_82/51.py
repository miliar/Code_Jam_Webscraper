#!/opt/local/bin/python

import string
import sys

input_it = iter(sys.stdin.readlines())
T = int(input_it.next())

for case in range(T):
    (C, D) = tuple(int(i) for i in input_it.next().split())
    sellers = [] # a list of seller positions
    needed_times = [] # a list of lists of times needed to spread
    for point in range(C):
        (P, V) = tuple(int(i) for i in input_it.next().split())
        for seller in range(V):
            for (i, pos) in enumerate(sellers): # all previous sellers
                needed_distance = D * (len(needed_times[i]) + 1)
                distance = P - pos
                needed_time = float(needed_distance - distance) / 2 if needed_distance > distance else 0
                needed_times[i].append(needed_time)
            sellers.append(P)
            needed_times.append([])

    max_time_needed = max(max(times) for times in needed_times if times)

    print 'Case #%s: %s' % (case + 1, max_time_needed)

