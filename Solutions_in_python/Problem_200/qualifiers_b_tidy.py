#!/usr/bin/env python
import sys
import re

exp = re.compile("^[0]*[1]*[2]*[3]*[4]*[5]*[6]*[7]*[8]*[9]*$")

def is_tidy(n):
    return exp.match(n)

def rem_zeros(n):
    for i in range(len(n)):
        if n[i] is not "0":
            return n[i:]
    return n

def process(line):
    print "=== INPUT : " + line
    num = list(line)
    numstr = "".join(num)
    while not is_tidy(numstr):
        curr = 0
        for i in range(len(num)):
            d = num[i]
            # print "i = " + str(i) + "; curr = " + str(curr) + "; d = " + d
            if int(d) < curr:
                # down!
                # print "old = " + num[i-1]
                num[i-1] = str((int(num[i-1]) - 1) % 10)
                # print "new = " + num[i-1]
                # import ipdb; ipdb.set_trace()
                for j in range(i, len(num)):
                    num[j] = str(9)
                break
            curr = int(d)
        numstr = "".join(num)
        print numstr
        
    return rem_zeros(numstr)

with open(sys.argv[2], "w") as fout:
    with open(sys.argv[1]) as fin:
        c = -1
        for line in fin:
            c += 1
            if c == 0:
                continue
            ans = process(line[:-1])
            fout.write("Case #{}: {}\n".format(c, ans))
