import sys
sys.stdout = open("out.txt", "w")


def solve(x):
    y=x.split()
    s, k = list(y[0]), int(y[1])
    ans = 0
    for i in range(len(s)-k+1):
        if s[i]=='-':
            ans+=1
            for j in range(i, i+k):
                if s[j]=='+':
                    s[j]='-'
                else:
                    s[j]='+'

    for i in range(len(s)-k+1, len(s)):
        if s[i]=='-':
            ans='IMPOSSIBLE'
            break

    return str(ans)


lines = []

with open("A-large.in", "r") as f:
    lines = f.readlines()

n = int(lines[0])

for i in range(1, n+1):
    ans = solve(lines[i].strip())
    print("Case #{}: {}".format(i, str(ans)))
