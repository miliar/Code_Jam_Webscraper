import sys 
from math import *
lines = sys.stdin.readlines()
for i in range((int(lines[0]))):
    N = int(lines[3*i+1])
    l1 = sorted([float(x) for x in lines[3*i+2].split()], reverse=True)
    l2 = sorted([float(x) for x in lines[3*i+3].split()], reverse= True)
    m1 = 0
    for j in range(len(l1)-1, -1,-1):
        s1 = l1[:len(l1)-j]
        s2 = l2[-len(l2)+j:]
        tmp  = 0
        for k in range(len(l1)-j):
            if (s1[k] > s2[k]): tmp += 1
        if tmp > m1: m1 = tmp
    m2 = 0
    for j in range(len(l1)):
        if l2[0] < l1[j]:
            l2.remove(l2[-1])
            m2 += 1
        else:
            tmp = [x for x in l2 if x > l1[j]]
            l2.remove(tmp[-1])
    print "Case #"+str(i+1)+":", m1, m2
