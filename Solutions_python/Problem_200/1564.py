T = int(input())
for t in range(T):
    N = list(input())
    i = 0
    sorted = True
    while i < len(N) - 1:
        if int(N[i]) <= int(N[i+1]):
            i += 1
        else:
            sorted = False
            break
    if not sorted:
        while i != 0 and int(N[i]) == int(N[i - 1]):
            i -= 1
        N[i] = int(N[i]) - 1
    for it in range(i + 1, len(N)):
        N[it] = '9'
    if N[0] == 0:
        del N[0]
    print('Case #{}: {}'.format(t + 1, ''.join(str(e) for e in N)))
