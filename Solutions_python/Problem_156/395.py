

def best_effort(pancakes, maxv, i):
    splits = 0
    for p in filter(lambda x: x > i, pancakes):
        splits += p//i - 1
        if p % i != 0:
            splits += 1
    return splits + i


testcases = int(input())

for t in range(testcases):
    int(input())
    pancakes = list(map(int, input().split()))
    maxv = max(pancakes)
    result = maxv
    for i in range(1, maxv):
        best_local = best_effort(pancakes, maxv, i)
        result = min(result, best_local)
    print("Case #%d: %d" % (t+1, result))
