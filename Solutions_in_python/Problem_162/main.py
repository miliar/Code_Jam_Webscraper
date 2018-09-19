def rev(n):
    return int(str(n)[::-1])

cache = [1, 1]
cachemax = 1

def solve(N):
    global cache
    global cachemax
    for i in range(cachemax + 1, N+1):
        cachemax += 1
        r = rev(i)
        if r < i and rev(r) == i:
            cache.append(min(cache[i-1], cache[r]) + 1)
        else:
            cache.append(cache[i-1] + 1)
    return cache[N]

tcnum = int(input())

for tc in range(1, tcnum+1):
    N = int(input())
    print("Case #{}: {}".format(tc, solve(N)))
