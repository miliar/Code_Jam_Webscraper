#!/usr/bin/python3
def inverse(s, j, k):
    l = list(s)
    for i in range(k):
        l[j+i] = '+' if l[j+i] == '-' else '-'
    return ''.join(l)

def solve(s, k):
    r = 0
    while True:
        j = s.find('-')
        if j == -1:
            return r
        elif j > len(s) - k:
            return 'IMPOSSIBLE'
        r = r + 1
        s = inverse(s, j, k)

n = int(input())
for t in range(n):
    s, k = input().split()
    print('Case #{}: {}'.format(t+1, solve(s, int(k))))
