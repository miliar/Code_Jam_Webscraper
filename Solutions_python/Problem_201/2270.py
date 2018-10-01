import sys

def available_stalls(stalls):
    ans = []
    for i in range(len(stalls)-1):
        s = int((stalls[i] + stalls[i+1])/2)
        a = s - stalls[i] - 1
        b = stalls[i+1] - s - 1
        ans.append((min(a, b), max(a, b), len(stalls) - s, s, i))

    return sorted(ans)

def test():
    N, K = tuple(map(int, sys.stdin.readline().strip().split()))
    stalls = [-1, N]
    available = available_stalls(stalls)
    next_available = []
    for k in range(K-1):
        if len(available) == 0:
            stalls.sort()
            available = available_stalls(stalls)
        n = available.pop()
        stalls.append(n[3])

    if len(available) == 0:
        stalls.sort()
        available = available_stalls(stalls)

    #print(stalls)
    #print(available)
    n = available.pop()
    return (n[1], n[0])

T = int(sys.stdin.readline())
for t in range(T):
    ans = test()
    print('Case #{}: {} {}'.format(t+1, ans[0], ans[1]))
