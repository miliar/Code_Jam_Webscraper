T = int(input().split()[0])

for i in range(T):
    N = [int(x) for x in input().split()[0]]
    h = [0 for i in range(10)]
    h[N[0]] += 1
    for j in range(1, len(N)):
        if N[j] >= N[j-1]:
            h[N[j]] += 1
            continue
        else:
            t = N[j-1] - 1
            if t > 0:
                h[t] += 1
                h[t+1] = 0
                h[9] = len(N) - sum(h)
                break
            else:
                h = [0 for i in range(10)]
                h[9] = len(N) - 1
                break
    if len(N) == 1:
        f = N[0]
    else:
        t = [str(x)*y for x,y in enumerate(h)]
        f = int(''.join(t))
    print('Case #{0}: {1}'.format(i+1, f))
