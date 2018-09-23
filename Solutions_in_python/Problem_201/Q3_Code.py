from math import ceil
import sys

def solve(caseNum, n, k):
    ans = query(n, k)
    print "Case #{}: {} {}".format(caseNum, ans[0], ans[1])


def query(n, k):
    if k == n: return (0, 0)
    if k == 1: return (n/2, n/2-1) if n%2 == 0 else (n/2, n/2)
    if k == 2: return query(n/2, 1)
    # k is even
    if k%2 == 0:
        return query(n/2, k/2)

    # k is odd
    if n%2 == 0: return query(n/2-1, k/2)
    return query(n/2, k/2)



t = int(input())  # read a line with a single integer

caseNum = 1
for line in sys.stdin:
    digits = line.split(' ')
    n, k= int(digits[0]), int(digits[1])
    solve(caseNum, n, k)
    caseNum += 1
