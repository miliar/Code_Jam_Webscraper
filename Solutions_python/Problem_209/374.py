# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
import math
pi = math.pi
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    N, K = [int(s) for s in input().strip().split()]
    listOfRiHi = []
    maxElement = (0,0,0)
    rank = -1
    for j in range(N):
        ri, hi = [int(s) for s in input().strip().split()]  # read a list of integers, 2 in this case

        value = (ri*hi, ri, ri*hi*2 + ri*ri)
        if value[2] > maxElement[2]:
            rank = j
            maxElement = value
        listOfRiHi.append((ri*hi, ri, ri*hi*2 + ri*ri))
    del listOfRiHi[rank]
    thisTable = list(sorted(listOfRiHi, key=lambda x: -x[0]))[:(K-1)]
    thisTable.append(maxElement)
    MaxR = list(sorted(thisTable, key=lambda x: x[1]))[-1][1]
    result = pi*(MaxR*MaxR + 2*sum(list(map(lambda x:x[0], thisTable))))
    print("Case #%s: %.6f" % (i, result))
    # check out .format's specification for more formatting options
