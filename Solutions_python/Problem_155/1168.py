# Python 3
t = int(input())
for i in range(t):
    ms, s = input().split()
    m = int(ms)
    tot = 0
    need = 0
    for j, n in enumerate(list(s[:m+1])):
        if tot < j:
            need += j-tot
            tot += j-tot
        tot += int(n)
    print("Case #" + str(i+1) + ": " + str(need))
