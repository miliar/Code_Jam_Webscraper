from decimal import *
from math import log10
from collections import deque

in_file = open('B-large.in', 'r')
out_file = open('finish.in', 'w')
temp = {}
getcontext().prec = 20


##k = Decimal(allsuc * (left + back + 1) + (1 - allsuc) * ((left + back + 1) + arr1[1] + 1))


def solve(n):
    count = 0
    k = str(n)
    i = 0
    while int(''.join(sorted(k))) != int(k):
        for i in range(len(k) - 1):
            if k[i] > k[i + 1]:
                k = int(k) - int(k[i + 1:]) - 1
                k = str(k)
                break
    return int(k)

p = []
for line in in_file:
    p.append(line)
n = p[0]
q = 1
i = 1
answer = None
ques = []
getcontext().prec = 20
while q < len(p):
    m = p[q].strip().split()
    answer = solve(int(m[0]))
    print("Case #%d: " % (i) + str(answer))
    i += 1
    q += 1
