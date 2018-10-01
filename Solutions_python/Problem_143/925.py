def solve(a, b, k):
    solutions = 0
    for i in range(a):
        for j in range(b):
            if i & j < k:
                solutions += 1
    return solutions

cases = int(input())
for case in range(cases):
    a, b, k = (int(num) for num in input().split())
    print("Case #{}: {}".format(case + 1, solve(a, b, k)))