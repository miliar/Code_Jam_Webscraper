from math import *
import os
os.chdir("/Users/Bastiaan/Documents")
c = open("B3.in").read()
d = c.split("\n")
e = int(d[0])
del(d[0])
def non(a):
    t = a[0]
    for b in str(a):
        if int(b) < int(t):
            return False
        else:
            t = b
    return True
for i in range(e):
    for s in range(int(d[i]),-1,-1):
        if non(str(s)):
            print("Case #" + str((i+1)) + ":" + " "  + str(s))
            break
