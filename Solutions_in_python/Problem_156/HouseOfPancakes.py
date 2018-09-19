'''
Created on 11.04.2015

@author: uscheller
'''
import sys
import math


def move(l, positions, largest):
    time_move = largest
    for divisor in range(2, int(math.sqrt(largest)) + 1):
        move_l = l[:]
        temp = 0
        for pos in positions:
            result = largest / divisor
            rest = result + (largest % divisor)
            move_l[pos] = rest
            for _ in range(divisor - 1):
                move_l.append(result)
                temp += 1
        temp += solve(move_l)
        time_move = min(time_move, temp)
    return time_move

def solve(l):
    largest = max(l)
    if largest == 0:
        return 0
    time_eat = largest #1 + solve([max(0, x - 1) for x in l])
    
    if largest > 1:
        positions = [i for i, j in enumerate(l) if j == largest]
        time_move = move(l, positions, largest)
    else:
        time_move = time_eat
    
    return min(time_eat, time_move)

def go_through(data):
    data = data[1:]
    s = ""
    case = 1
    while len(data) > 0:
        l = [int(x) for x in data[1].split()]
        D = int(data[0])
        assert D == len(l)
        data = data[2:]
        s += "Case #%d: %d\n" % (case, solve(l))
        case += 1
    return s[:-1] # remove newline

if __name__ == '__main__':
    print go_through(open(sys.argv[1]).readlines())