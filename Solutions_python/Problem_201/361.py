import collections
def f(a,b):
    d = {a: 1}
    return recurse(d, b)


def recurse(d, k):
    newDict = collections.defaultdict(int)

    for key in reversed(sorted(d)):
        val = d[key]
        key -= 1
        low = key // 2
        high = key - low
        if k <= val:
            return "%s %s" % (high, low)
        k -= val
        newDict[low] += val
        newDict[high] += val
    return recurse(newDict, k)


T = int(input())
for case in range(1, T+1):
    a,b = map(int,input().split())
    ans = f(a,b)
    print("Case #%s: %s" % (case, ans))

