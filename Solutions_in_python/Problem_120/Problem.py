#!/bin/env python3

from decimal import Decimal
import math


T=0
test_case_no = 1

r=0
t=0

f = open("result_small.txt", "w")

for line in open("./A-small-attempt0.in"):
    if T == 0:
        T = int(line)
    else:
#        r, t = (float(x) for x in line.split())
        r, t = (Decimal(x) for x in line.split())

        print(r,t)

        tmp = Decimal(2)*r - Decimal(1)
        y = Decimal.sqrt((t + (tmp)**2 / Decimal(8)) / Decimal(2)) - (tmp / Decimal(4))
#        y = math.sqrt((t + (2*r - 1)**2 / 8.0) / 2.0) - ((2*r - 1) / 4.0)

        print(math.floor(y))

        f.write("Case #{0}: {1}\n".format(test_case_no, math.floor(y)))
        test_case_no += 1

f.close()

