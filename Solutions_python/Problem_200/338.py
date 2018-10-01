#!/opt/local/bin/python

import sys
import re

def doit(lst):
    if len(lst) == 1:
        return lst

    i = 0

    while i + 1 < len(lst):
        if lst[i] > lst[i+1]:
            break
        i += 1

    if i + 1 == len(lst):
        return lst

    problem = i

    r = '9' * (len(lst) - i - 1)

    r = str(int(lst[i])-1) + r
    
    i -= 1
    while lst[i] == lst[problem] and i >= 0:
        r = r + '9'
        i -= 1

    if i >= 0:
        r = lst[:i+1] + r
    # elif lst[0] == '1':
    #    q = q[1:]
    s = re.sub("^0*", "", r)

    return s
    

T = int(sys.stdin.readline())
for casenum in range(T):
    data = sys.stdin.readline()

    n = doit(data[:-1])




    print("Case #" + str(casenum + 1) + ": " + n ) # + "\t[" + data[:-1] + "]")
