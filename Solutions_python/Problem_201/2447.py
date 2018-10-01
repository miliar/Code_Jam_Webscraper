import sys
import math as m

iMaxStackSize = 20000
sys.setrecursionlimit(iMaxStackSize)

def iterateOverList(list):
    maxLength = list.pop()
    return sorted(list + [m.floor((maxLength - 1)/2.)] + [m.ceil((maxLength - 1)/2.)])

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    numberOfToilets, persons = [s for s in input().split(" ")]  # read a list of integers, 2 in this case
    numberOfToilets = int(numberOfToilets)
    persons = int(persons)
    list = [numberOfToilets]
    for k in range(persons - 1):
        list = iterateOverList(list)
    maxLength = list.pop()
    print("Case #{}: {} {}".format(i, m.ceil((maxLength - 1)/2.), m.floor((maxLength - 1)/2.)))
  # check out .format's specification for more formatting options
