import sys

def solve():
    a, b = (int(x) for x in sys.stdin.readline().strip().split(" "))
    cnt = 0
    for n in range(a, b):
        s = str(n)
        check = set()
        l = len(s)
        for i in range(1, l):
            num = int(s[i:] + s[:i])
            if num > n and num <= b and num not in check:
                cnt += 1
                check.add(num)
    return cnt

T = int(sys.stdin.readline())
for testCase in range(1, T+1):
    print("Case #%i:" % testCase, solve())
