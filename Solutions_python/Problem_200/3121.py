t = int(input())

for T in range(t):
    v = list(input())
    v = [int(x) for x in v]
    n = len(v)
    i = n-1
    m = 9 
    while i > 0:
        if v[i-1] > v[i]:
            if v[i] == 0:
                v[i] = 9
                for j in range(i,n):
                    v[j] = 9
                v[i-1]-=1
            else:
                m = max(m,v[i])
                for j in range(i,n):
                    v[j] = max(v[j],m)
                v[i-1]-=1
        i-=1

    print("Case #%d: " % (T+1), end = '')
    for x in v:
        if (x != 0):
            print(x,end='')
    print()
