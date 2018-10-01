from __future__ import print_function
import sys

cases = int(sys.stdin.readline())
n = 1
data1, data2 = [[[] for i in range(4)] for j in range(4)], [[[] for i in range(4)] for j in range(4)]

for n in range(1, cases+1):
    a = int(sys.stdin.readline())
    for i in range(4):
        data1[i] = [int(num) for num in sys.stdin.readline().strip().split()]
    b = int(sys.stdin.readline())
    for i in range(4):
        data2[i] = [int(num) for num in sys.stdin.readline().strip().split()]

    aset = set(data1[a-1])
    bset = set(data2[b-1])
    r = aset.intersection(bset)
    if len(r)==1:
        print('Case #'+repr(n)+': '+repr(r.pop()))
    elif len(r)>1:
        print('Case #'+repr(n)+':'+' Bad magician!')
    else:
        print('Case #'+repr(n)+': Volunteer cheated!')
