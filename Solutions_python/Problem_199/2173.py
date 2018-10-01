def flip(a, n):
    for i in range(n):
        if(a[i] == '-'):
            a[i] = '+'
        else:
            a[i] = '-'
    return a

t = int(input())
a = []

for i in range(t):
    s = input().split()
    k = int(s[1])
    s = list(s[0])
    a += [1]
    n = 0

    for j in range(len(s)):
        if(s[j] == '-'):
            if(j + k <= len(s)):
                s[j:j+k] = flip(s[j:j+k],k)
                n += 1
                #print("Debug N=\n", n, "UAO I=", i)
            else:
                a[i] = "IMPOSSIBLE"
    if(a[i] != "IMPOSSIBLE"):
        a[i] = n

for i in range(t):
    print("Case #" + str(i+1) + ": " + str(a[i]))

