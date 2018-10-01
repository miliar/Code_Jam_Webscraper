
__author__ = 'sergeyy'
import time
import sys

def checkR(c,f,x, s):
    if x/s - (c/s + x/(s+f))  < 0.0000001:
        return x/s
    else :
        return  c/s + checkR(c,f,x,s+f)


def check(c,f,x):
    if x-c < 0.0000001:
        return x/2
    else:
        return checkR(c,f,x,2)

sys.setrecursionlimit(99900)
case = 1
m = [["."]*4]*4
with open('input.txt', 'r') as fin:
    with open('output.txt', 'w') as fout:
        cnt = int(fin.readline())
        for i in range(1, cnt+1):
            line = fin.readline()
            rcm = line[:-1:].split(' ')
            c = float(rcm[0])
            f = float(rcm[1])
            x = float(rcm[2])

            oline = ''
            oline = 'Case #' + str(i) +': ' + str(check(c, f ,x)) +'\n'
            fout.write(oline)




