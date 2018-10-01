import sys
name = "A-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

def switcher(j, k):
    for i in range(j, j+k):
        if s[i]=='+':
            s[i]='-'
        else:
            s[i]='+'

for testCase in range(1, testCases + 1):
    s, k=input().strip().split()
    k=int(k)
    s=list(s)
    ans=0
    for i in range(len(s)-k+1):
        if s[i]=='-':
            switcher(i, k)
            ans+=1
    possible=True
    for i in s:
        if i=='-':
            possible=False
            break
    if possible:
        print("Case #%s: %s" % (testCase, ans))
    else:
        print("Case #%s: %s" % (testCase, 'IMPOSSIBLE'))

