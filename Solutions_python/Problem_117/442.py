num = int(input())
for t in range(num):
    print('Case #$: '.replace('$', str(t + 1)), end = '')
    a = []
    flag = 1
    b = []
    n, m = list(map(int, input().split()))
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(a[j][i])
        b.append(temp)
    for i in range(n):
        for j in range(m):
            if a[i][j] != max(a[i]) and b[j][i] != max(b[j]) and flag:
                print('NO')
                flag = 0
    if flag:
        print('YES')
