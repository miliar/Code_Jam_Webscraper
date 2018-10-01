#viva venezuela
t = int(input())
for m in range(t):
    n = list(input())
    i = len(n)-2
    while(i >= 0):
        if n[i] > n[i+1]:
            n[i] = str(int(n[i])-1)
            n[i+1] = "9"
            for x in range(i+2,len(n)):
                n[x] = "9"
        i-=1
    a = ""
    for i in n:
        a += i
    print("Case #" +str(m+1) + ": " + str(int(a)))
