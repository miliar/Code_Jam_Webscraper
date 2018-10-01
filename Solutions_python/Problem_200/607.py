import sys

def ri():
    return map(int, sys.stdin.readline().split())


T = int(input())

def sol(i, nn, b):
    global n
    if i == len(n):
        return nn[:]
    if b == True:
        for j in range(i, l):
            nn[j] = 9
        return nn[:]
    else:
        ncandi = nn[:]
        if i == 0:
            e = -1
        else:
            e = nn[i-1] -1
        for j in range(nn[i], e, -1):
            ncandi[i] = j
            ans = sol(i+1, ncandi, j != n[i])
            if ans != []:
                return ans[:]
        return []


for i in range(T):
    n = input()
    n = [int(x) for x in n]
    ncandi = n[:]
    l = len(n)
    ans = sol(0, n, False)
    ans = "".join(map(str, ans)).strip('0')
    print("Case #%d: %s"%(i+1, ans))
