import sys

def reverse(s,start,k):
    for i in range(start, start+k):
        if s[i] == '-':
            s[i] = '+'
        else:
            s[i] = '-'

t = int(sys.stdin.readline())
for t0 in range(t):
    res = 0
    s, k = sys.stdin.readline().split(' ')
    s = [char for char in s]
    k = int(k)
    for i in range(len(s) - k + 1):
        if s[i] == '-':
            res += 1
            reverse(s, i, k)
    for i in range(len(s) - 1, len(s) - 1 - k, -1):
        if s[i] == '-':
            res = - 1
            break
    print("Case #" + str(t0 + 1) + ': ' + ("IMPOSSIBLE" if res == -1 else str(res)))



