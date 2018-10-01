def flip(s, o, l):
    for i in range(l):
        s[o+i] = '-' if s[o+i] == '+' else '+'
    return s

def solve(s, k):
    ss = list(s)
    n = 0
    for i in range(len(s)-k+1):
        if ss[i] == '-':
            ss = flip(ss, i, k)
            n += 1
    for i in range(k):
        if ss[len(s)-1-i] == '-':
            return None
    return n

t = int(input())
for i in range(t):
    line = input().split(" ")
    S = line[0]
    K = int(line[1])
    r = solve(S, K)
    res = r if r != None else "IMPOSSIBLE"
    print("Case #" + str(i+1) + ":", res)
