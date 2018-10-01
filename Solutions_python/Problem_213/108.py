import numpy as np
from itertools import combinations
from math import ceil, floor, pi
from functools import lru_cache


def get_num_rider(N, C, tickets):
    tickets_per_cust = np.zeros(C)
    tickets_per_seat = np.zeros(N)
    for seat, c in tickets:
        tickets_per_cust[c] += 1
        tickets_per_seat[seat] += 1

    density = np.cumsum(tickets_per_seat) / (np.arange(N)+1)
    min_rides = np.max(density)
    min_rides = max(min_rides, max(tickets_per_cust))

    return min_rides



def rollercoaster(N, C, M, tickets):
    """
    N:          seats
    C:          customers
    M:          tickets
    tickets:    (position, buyer)           sorted
    """
    num_rides = get_num_rider(N, C, tickets)

    tickets_per_cust = np.zeros(C)
    tickets_per_seat = np.zeros(N)
    for seat, c in tickets:
        tickets_per_cust[c] += 1
        tickets_per_seat[seat] += 1

    promotions_per_seat = np.maximum(0, tickets_per_seat - num_rides)
    num_promotions = sum(promotions_per_seat)

    # seats = np.zeros((num_rides, N))
    # customer_in_ride = np.zeros((num_rides, C))
    # num_rides = 0
    #
    # for seat, c in tickets:
    #     ride = 0
    #     while seats[ride, seat] or customer_in_ride[ride]:
    #         ride += 1



    return num_rides, num_promotions


if __name__ == '__main__':
    # PATH_IN = 'sample.in'
    PATH_IN = 'B-small-attempt0.in'
    # PATH_IN = 'A-large-practice.in'
    PATH_OUT = PATH_IN[:-3] + '.out'

    f_in = open(PATH_IN, 'r')
    f_out = open(PATH_OUT, 'w')

    T = int(f_in.readline())
    for t in range(T):
        line = f_in.readline().split()

        N = int(line[0])
        C = int(line[1])
        M = int(line[2])
        print(N, C, M)

        tickets = []
        for i in range(M):
            line = f_in.readline().split()
            tickets.append((int(line[0])-1, int(line[1])-1))

        tickets = sorted(tickets)
        print(tickets)

        runs, promos = rollercoaster(N, C, M, tickets)
        # runs = get_num_rider(N, C, tickets)

        print('Case #%i: %i %i' % (t + 1, runs, promos))
        f_out.write('Case #%i: %i %i\n' % (t + 1, runs, promos))
