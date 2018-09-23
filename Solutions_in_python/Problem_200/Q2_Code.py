import sys
from collections import deque


def solve(caseNum, s):
    print "Case #{}: {}".format(caseNum, last_tidy(str(s)))

def last_tidy(num):
    """
    num: str
    """
    n = len(num)
    n_sorted = 1
    while n_sorted < n and num[n_sorted] >= num[n_sorted-1]: n_sorted+=1
    if n_sorted == n: return num
    pre = int(num[:-1])-1
    if pre == 0: return '9'
    return last_tidy(str(pre)) + '9'


t = int(input())  # read a line with a single integer

caseNum = 1
for line in sys.stdin:
    m = int(line)
    solve(caseNum, m)
    caseNum += 1
