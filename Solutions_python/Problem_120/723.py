__author__ = 'sergeyy'
import time
import math

def prebuild(m):
    ret = [0*m]
    for i in range(m):
        ret.append((i+1)**2-i**2)
    return ret


def solve(r, t):
    ret = 0
    # while t>=0:
    #     r = r +2
    #     t = t - a[r]
    #     ret = ret +1
    while t>=0:
        p = (r+1)**2 - r**2
        r = r +2
        t = t - p
        ret = ret +1
    return str(ret -1)


time.clock()
# a = prebuild(1000)
with open('input.txt', 'r') as fin:
   with open('output.txt', 'w') as fout:
      cnt = int(fin.readline())
      for case in range(1, cnt+1):
         r, t = [int(x) for x in fin.readline().split()]
         oline = ''
         oline = 'Case #' + str(case) +': ' + solve(r, t) +'\n'
         fout.write(oline)
print (time.clock())




