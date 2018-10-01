for dskjfk in range(int(input())):
    s, m = input().split()
    s = list(s)
    n = len(s)
    m = int(m)
    cnt = 0
    for i in range(n-m+1):
        if s[i] == '-':
            cnt += 1
            for j in range(m):
                s[i+j] = '+' if s[i+j]=='-' else '-'
    print('Case #{}: '.format(dskjfk + 1), end='')
    for j in range(m):
        if s[n-1-j] == '-':
            cnt = -1
            break
    print(cnt if cnt >= 0 else 'IMPOSSIBLE')
