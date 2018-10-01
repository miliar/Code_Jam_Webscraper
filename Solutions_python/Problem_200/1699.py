"""https://code.google.com/codejam/contest/dashboard?c=3264486#s=p1"""

from collections import deque

def solve(n):
    q = deque()
    q.append(0)
    res = 1
    while q:
        num = q.popleft()
        res = max(res, num)
        digit = max(1, num % 10)
        for i in range(digit, 10):
            t = num * 10 + i
            if t <= n:
                q.append(t)
    return res

if __name__ == '__main__':
    for i in range(int(input())):
        res = solve(int(input()))
        print("Case #{}: {}".format(i + 1, res))
