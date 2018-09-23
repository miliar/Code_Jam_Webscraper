import sys
# C:\Users\Harshit\PycharmProjects\Test36\A-small.out
name = "C-small-1-attempt1"
path = ""
sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    n, k = list(map(int, input().split()))
    l = [n]
    leng = 1
    for i in range(k):
        v=max(l)
        x = int(v / 2)
        if (v % 2 == 0):
            l.append(x)
            l.append(x - 1)
            l.remove(v)
        else:
            l.append(x)
            l.append(x)
            l.remove(v)
        leng += 1
    ans=str(l[leng-2])+" "+str(l[leng-1])
    print("Case #" + str(testCase) + ": " +ans)