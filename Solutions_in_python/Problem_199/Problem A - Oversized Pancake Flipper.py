t = int(input())

for tc in range(t):
    s, k = input().split()
    k = int(k)
    lst = []
    for c in s:
        if c == '+':
            lst.append(True)
        else:
            lst.append(False)

    ct = 0
    isPossible = True
    for i in range(len(lst)):
        if not lst[i]:
            if i + k - 1 >= len(lst):
                isPossible = False
                break
            for j in range(k):
                lst[i + j] ^= True
            ct += 1

    tc += 1
    if isPossible:
        print('Case #{}: {}'.format(tc, ct))
    else:
        print('Case #{}: IMPOSSIBLE'.format(tc))
