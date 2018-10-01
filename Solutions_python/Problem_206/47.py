n = int(input())

def solve():
    d, n = map(int, input().split())
    a = [list(map(int, input().split())) for i in range(n)]
    a.sort()
    res = float('+inf')
    for x, v in a:
        res = min(res, d*v/(d-x))
    return res

for i in range(1, n+1):
    print("Case #%d:" % i, solve())
