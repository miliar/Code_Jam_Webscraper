
t = int(input())

def ulta(c):
    return '+' if c == '-' else '-'

for cas in range(1, t+1):
    s, k = input().split()
    k = int(k)
    s = list(s)

    # process in left-to-right order
    flips = 0
    for pos in range(0, len(s)-k):
        if s[pos] == '-':
            flips += 1
            for subpos in range(k):
                s[pos+subpos] = ulta(s[pos+subpos])

    last_k = s[-k:]
    last_k = ''.join(last_k)

    if last_k == '-'*k:
        print('Case #{}: {}'.format(cas, flips+1))
    elif last_k == '+'*k:
        print('Case #{}: {}'.format(cas, flips))
    else:
        print('Case #{}: IMPOSSIBLE'.format(cas))

