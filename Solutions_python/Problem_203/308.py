T = int(input())
for I in range(1, T + 1):
    r, c = map(int, input().split())
    res = [''] * r
    start = [0] * r
    meaning = [''] * r
    mr = -1
    for i in range(r):
        for j, letter in enumerate(input()):
            if letter != '?':
                res[i] += letter * (j - start[i] + 1)
                start[i] = j + 1
                meaning[i] = letter
                mr = i
        if meaning[i] == '':
            continue
        if start[i] != c:
            res[i] += meaning[i] * (c - start[i])
        k = i - 1
        while k >= 0 and meaning[k] == '':
            res[k] = res[i]
            meaning[k] = '!'
            k -= 1

    if meaning[-1] == '':
        k = r - 1
        while k >= 0 and meaning[k] == '':
            res[k] = res[mr]
            k -= 1

    print('Case #%s:' % I)
    for s in res:
        print(s)
