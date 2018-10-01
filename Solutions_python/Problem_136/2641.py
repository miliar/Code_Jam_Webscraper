import sys
from math import sqrt, floor, ceil
from numpy import transpose


def result(lst):
    if len(lst) == 0:
        return "Volunteer cheated!"
    elif len(lst)>1:
        return "Bad magician!"
    else:
        return str(lst[0])

def solve(c, f, x):
    N = ceil(x/c-2/f-1)
    if N<0:
        N = 0
    total_time = 0
    for n in range(0,N):
        total_time+=c/(2+n*f)
    total_time+=x/(2+N*f)
    return total_time

file = sys.argv[1]
with open(file) as input:
    with open("output.txt", "w") as output:
        numcases = int(input.readline())
        for casenum in range(1,numcases+1):
            c,f,x = tuple(map(float, input.readline().split()))
            msg = "Case #{0}: {1:.7f}\n".format(str(casenum), solve(c, f, x))
            output.write(msg)
