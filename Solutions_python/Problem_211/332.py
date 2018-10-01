import sys
import math
from collections import defaultdict
import heapq

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

name = sys.argv[1]
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

T = int(input())
          
for testCase in range(1, T + 1):
    eprint("Case #", testCase)
    n, k = [int(x) for x in input().split()]    
    u = float(input())
    A = [float(x) for x in input().split()]
    while u > 0.0:
        s = sorted(set(A))
        eprint(s)
        mini = s[0]
        if len(s) > 1:
            second = s[1]
        else:
            second = 1.0
        eprint("mini", mini, "second", second)
        cnt_minis = 0
        for a in A:
            if a <= mini:
                cnt_minis += 1
        if (second - mini) * cnt_minis <= u:
            add = (second - mini) 
        else:
            add = u / cnt_minis
        eprint("add", add)
        if add == 0:
            break
        NEW_A = []
        for a in A:
            if a <= mini:
                NEW_A.append(a + add)
                u -= add
            else:
                NEW_A.append(a)
        A = NEW_A
        
    eprint(A)
    prob = 1.0
    for a in A:
        prob *= a
    print("Case #" + str(testCase) + ": %.7f" % prob)
        


