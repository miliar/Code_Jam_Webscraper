from copy import deepcopy
from collections import namedtuple, defaultdict, Counter
import functools
import numpy as np
import common 
from common import *


def parse(lines):
    N, C, M = lines.next().split()
    N, C, M = int(N), int(C), int(M)
    
    tickets = defaultdict(list)
    for _ in range(M):
        P, B = lines.next().split()
        P, B = int(P), int(B)
        tickets[B] += [P]
    
    return N, dict(tickets)

####

def solve(input):
    N, tickets = input
    tickets = deepcopy(tickets)
    if len(tickets) == 1:
        trains = len(tickets.values()[0])
        promotions = 0
        return '%s %s' % (trains, promotions)
    
    A = tickets[1]
    B = tickets[2]

    if len(A) > len(B):
        more, less = A, B
    else:
        more, less = B, A

    available = Counter([])
    for n in more:
        seats = range(1, N+1)
        seats.remove(n)
        for s in seats:
            available[s] += 1

    last = []
    for t in less:
        if available[t] > 0:
            available[t] -= 1
        else:
            last += [t]

    available2 = [[i]*n for i, n in available.items()]
    available2 = [b for a in available2 for b in a]
    available2 = sorted(available2)[::-1]

    m = max(less)
    available2 = [a for a in available2 if a < m]

    promotions = 0
    worst = list(last)
    for t in last:
        for seat in available2:
            if seat < t:
                promotions += 1            
                available2.remove(seat)
                worst.remove(t)
                break

    trains = len(worst) + len(more)

    return '%s %s' % (trains, promotions)


# def solve(input):
#     N, tickets = input
#     t = deepcopy(tickets)
#     promotions = 0
#     trains = 0
#     while True:
#         trains += 1
#         p, t = run_once(t, N)
#         promotions += p
#         if not t:
#             break

#     print '-' * 10
#     print trains, promotions
#     print '-' * 10
#     return '%s %s' % (trains, promotions)


# def run_once(tickets, N):
    
#     initial_tickets = deepcopy(tickets)
#     tickets = deepcopy(tickets)

#     # fill a ride

#     # get the best first
#     order = range(1,N+1)[::-1]
#     available = range(1, N+1)
#     customers = list(tickets)
#     for n in order:
#         matches = [c for c in customers if n in tickets[c]]
#         matches = sorted(matches, key=lambda c: -len(tickets[c]))
#         if matches:
#             available.remove(n)
#             tickets[matches[0]].remove(n)
#             customers.remove(matches[0])
#         print tickets, customers

#     # run promotions
#     order = list(available)[::-1]
#     losers = {c: tickets[c] for c in customers}

#     promotions = 0
#     for n in available:
#         # sort by (delta, number of tickets, c)
#         lottery = []
#         for c in losers:
#             for t in losers[c]:
#                 if t > n:
#                     lottery += [(t - n, len(losers[c]), c)]

#         lottery = sorted(lottery)
#         if lottery:
#             delta, ntickets, c = lottery[0]
#             tickets[c].remove(delta + n)
#             losers.pop(c)

#             promotions += 1

#     for c in tickets.keys():
#         if not tickets[c]:
#             tickets.pop(c)

#     print 'promotions', promotions
#     print 'tickets', tickets
#     return promotions, tickets


####

output_newline = False


def write(x):
    return write_cases(x, newline=output_newline)


def test(input=None, output=None):
    input = input or example_input
    output = output or example_output
    a_test = make_test(parse, solve, write)
    a_test(input, output)
    print 'ok'


def run(f):
    inputs = read_by_parser(f, parse)
    f2 = f + '.out'
    outputs = [format(solve(cake)) for cake in inputs]
    save_cases(f2, outputs, newline=output_newline)
    return outputs


##### 

example_input = \
"""5
2 2 2
2 1
2 2
2 2 2
1 1
1 2
2 2 2
1 1
2 1
1000 1000 4
3 2
2 1
3 3
3 1
3 3 5
3 1
2 2
3 3
2 2
3 1
"""

example_output = \
"""Case #1: 1 1
Case #2: 2 0
Case #3: 2 0
Case #4: 2 1
Case #5: 2 1
"""
