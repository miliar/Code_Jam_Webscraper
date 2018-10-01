# Google Code Jam : Qualification Round 2011 : Problem C. Candy Splitting
# https://code.google.com/codejam/contest/dashboard?c=975485#s=p2
# Python 2.6.5

import operator

def xor(a):
    return reduce(operator.xor, a)

def find_split(candies):
    if xor(candies) != 0:
        return "NO"
    else:
        return sum(candies) - min(candies)


def solve_case(t, case_str):
    candies = [int(c) for c in case_str.split()] 
    print "Case #" + str(t) + ": " + str(find_split(candies))


def solve():
    T = int(raw_input())
    for t in range(1, T + 1):
        raw_input()
        solve_case(t, raw_input())

solve()
