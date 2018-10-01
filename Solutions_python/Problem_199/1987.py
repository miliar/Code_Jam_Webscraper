def Flip(x):
    return "-" if x == "+" else "+"

def Solve(s, k):
    ans = 0
    for i in range(len(s)):
        if i + k <= len(s):
            if s[i] == "-":
                for j in range(k):
                    s[i + j] = Flip(s[i + j])
                ans += 1
    if "-" in s:
        return "IMPOSSIBLE"
    return str(ans)

numOfLines = int(raw_input())
for i in range(numOfLines):
    tmp = raw_input().split()
    S = tmp[0]
    K = int(tmp[1])
    print "Case #" + str(i+1) + ": " + Solve(list(S), K)

