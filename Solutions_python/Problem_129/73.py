##input = open('A-sample-input.txt', 'r')
##output = open('A-sample-output.txt', 'w')

##input = open('A-small-attempt0.in', 'r')
##output = open('A-small.out', 'w')

input = open('A-large.in', 'r')
output = open('A-large.out', 'w')

import math
from decimal import Decimal as D

def read_int():
    return int(input.readline().strip())

def read_ints():
    return [int(x) for x in input.readline().split()]

def read_float():
    return float(input.readline().strip())

def read_floats():
    return [float(x) for x in input.readline().split()]

def solve(N, M, oe_pairs):
    stations = {}
    reg_cost = 0
    for oe in oe_pairs:
        dist = oe[1] - oe[0]
        cost = dist * N - (dist - 1) * dist / 2
        reg_cost += cost * oe[2]
        if oe[0] not in stations.keys():
            stations[oe[0]] = [oe[2], 0]
        else:
            stations[oe[0]][0] += oe[2]
        if oe[1] not in stations.keys():
            stations[oe[1]] = [0, oe[2]]
        else:
            stations[oe[1]][1] += oe[2]
##    print reg_cost
    cards = []
    sorted_stations = sorted(stations.keys())
    old_station = sorted_stations[0]
    cards.append([stations[old_station][0],0])
    total = 0
##    print cards
    for i in range(1, len(sorted_stations)):
        new_station = sorted_stations[i]        
        advance = new_station - old_station
        old_station = new_station
        for card in cards:
            card[1] += advance
        if stations[new_station][0] > 0:
            cards.append([stations[new_station][0],0])
##        print cards
        getting_off = stations[new_station][1]
##        print getting_off
        while getting_off > 0:
            if cards[-1][0] > getting_off:
##                print 'some of the last group getting off'                
                c = cards[-1][1]
                cost = (c * N - c * (c-1) / 2) * getting_off
##                print 'cost =', cost
                total += cost                
                cards[-1][0] -= getting_off
                getting_off = 0
##                print cards
            elif cards[-1][0] == getting_off:
##                print 'all of the last cards off'
                c = cards[-1][1]
##                print 'c', c
                cost = (c * N - c * (c-1) / 2) * getting_off
                getting_off = 0
##                print 'cost =', cost
                total += cost
                cards.pop(len(cards) - 1)
##                print cards
            else:
##                print 'all of the last cards off + some more'
                c = cards[-1][1]
                cost = (c * N - c * (c-1) / 2) * cards[-1][0]
##                print 'cost =', cost
                total += cost
                getting_off -= cards[-1][0]
                cards.pop(len(cards)-1)
##                print cards
    return (reg_cost - total) % 1000002013
                
        
    
def main():
    num_cases = read_int()
    for case in range(1, num_cases+1):
        N, M = read_ints()
        oe_pairs = []
        for i in range(M):
            oe_pairs.append(read_ints())
##        if case == 1:
        solution = solve(N, M, oe_pairs)
        solution_string = "Case #%d: %s" %(case, solution)
        output.write(solution_string + "\n")
        print solution_string
        

main()
input.close()
output.close()
    
