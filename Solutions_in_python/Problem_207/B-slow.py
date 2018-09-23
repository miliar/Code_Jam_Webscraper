from itertools import permutations

def bad(a, b):
    return (a == (b+1)%7) or (b==(a+1)%7) or (a == b)

def is_good(l):
    for i in range(len(l)):
        if bad(l[i], l[i-1]):
            return False
    return True

def trans(a):
    return ['R', 'Y', 'B'][a]

t = int(input())

for tc in range(t):
    uc = [int(x) for x in input().split()][1::2]
    
    u = sorted(uc)
    if sum(u) < 2*u[-1]:
        print('Case #{}: {}'.format(str(tc+1), 'IMPOSSIBLE'))
        continue

    res = []
    prev = -1
    while(sum(uc)):
        a = -1
        m = -1
        for i, e in enumerate(uc):
            if i != prev and e>m:
                m = e
                a = i
        uc[a] -= 1
        prev = a
        res.append(a)

    if res[0] == res[-1]:
        res[-1], res[-2] = res[-2], res[-1]

    print('Case #{}: {}'.format(str(tc+1), ''.join(map(trans, res))))        
