f = open("Tidy Numbers.txt", "w")
T = int(input())
for i in range(T):
    N = input()
    n = int(N)
    mark = 0
    for j in range(len(N)-1):
        if int(N[j]) > int(N[mark]):
            mark = j
        if int(N[j]) > int(N[j+1]):
            n = N[:mark]+str(int(N[mark])-1)+'9'*(len(N)-mark-1)
            break
    n = int(n)
    f.write("Case #%d: %d\n"%(i+1,n))
f.close()
