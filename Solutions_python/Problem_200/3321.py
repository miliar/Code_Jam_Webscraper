#!/usr/bin/python

import sys
import time

data = open(sys.argv[1]).read().splitlines()
outfile = open(sys.argv[1] + ".out", 'w')

data.pop(0)
print data
case = 1
for row in data:

    # print "[!] ", row
    num = int(row)
    while True:
        # print num
        is_tidy = True
        tnum = num
        max_d = 9
        mod = 1
        while tnum > 0:
            #print mod
            d = tnum % 10
            if d > max_d:
                # print "!!!"
                is_tidy = False
                tnum = 0
            else:
                max_d = d
                tnum /= 10
                mod *= 10
        if is_tidy == False:
            num -= (num % mod)
            #print num
            num -= 1
            #time.sleep(1)
        else:
            out = "Case #%d: %d" % (case, num)
            print out
            outfile.write(out + "\n")
            break
    case += 1
