import sys, os, itertools
from functools import reduce
from types import *



def xor(x, y): return x^y

def bagvalue(L):
    if len(L) < 2:
        return sum(L)
    else:
        return reduce(xor, L)

t = int(sys.stdin.readline())
for i in range(t):
    phat_lewt = 0
    quantity = int(sys.stdin.readline())
    bag_of_candy = [int(s) for s in sys.stdin.readline().split()]
    for j in range(1, quantity):
        for subset in itertools.combinations(bag_of_candy, j):
            patrick_bag = subset
            sean_bag = list(bag_of_candy)
            for candy in patrick_bag:
                sean_bag.remove(candy)
            if bagvalue(patrick_bag) == bagvalue(sean_bag):
                value = sum(patrick_bag)
                if value > phat_lewt:
                    phat_lewt = value
    if phat_lewt == 0:
        result = "NO"
    else:
        result = phat_lewt
    print ("Case #%d:" % (i+1), result)
