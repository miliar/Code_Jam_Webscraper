def flip(n, i, k):
    for j in range(0, k):
        n[j+i] = '+' if n[j+i] == '-' else '-'
    return n

def solve(n, k):
    flips = 0
    i = 0
    while i <= len(n) - k:
        if n[i] == '-':
            flip(n, i, k)
            flips += 1
        i += 1
    if set(n) == set('+'):
        return flips
    else:
       return 'IMPOSSIBLE'

t = int(raw_input())
for i in xrange(1, t+1):
    n, m = raw_input().split(' ')
    m = int(m)
    print 'Case #{}: {}'.format(i, solve(list(n), m))
