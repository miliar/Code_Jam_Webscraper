#!/usr/bin/python
import math
from mpmath import *

for case in range(input()):
    n = int(raw_input())
    mp.dps = 1000 
    f = mpf((mpf(3) + mpf(5).sqrt())**n)
    s = nstr(f,1000).split(".")[0]
#    s= "%f" % (f)
#    s = s.split(".")[0]
    num = s[-3:]
    if len(num) == 2:
        num = "0"+num
    if len(num) == 1:
        num = "00"+num
    if len(num) == 0:
        num = "000"
    print "Case #%i: %s" % (case+1,num)
