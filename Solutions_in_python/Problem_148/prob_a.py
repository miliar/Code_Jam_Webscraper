from datetime import datetime
from collections import defaultdict, deque
# from math import sqrt
# from bintrees import RBTree
# from networkx import Graph

BEGIN_TIME = datetime.now()

# BIG = 1000 * 1000 + 3
# BIG = 1000 * 1000 * 1000 + 7
# BIG = int(3e12)
# MIN_ERROR = 1e-6

file_name = "A-small-attempt0"
file_name = "A-large"


f = open("../../../../" + file_name + ".in", "r")
# f = open("../test.txt")

w = open("../../../../" + file_name + ".out", "w")
TESTCASES = int(f.readline())

for T in range(1, TESTCASES + 1):
    print "Case #", T
    w.write("Case #" + str(T) + ": ")
    
    # read in info
    N, X = map(int, f.readline().split())
    s = sorted(map(int, f.readline().split()))

    bigi, i = N - 1, 0
    total = 0
    while True:
        while bigi > i and s[bigi] + s[i] > X:
            bigi -= 1
        if bigi <= i:
            break
        total += 1
        bigi -= 1
        i += 1

    w.write(str(N - total) + "\n")

    
    print "Elapsed Time: ", datetime.now() - BEGIN_TIME


