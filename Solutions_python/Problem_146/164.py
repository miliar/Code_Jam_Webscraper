from itertools import permutations

def valid(t):
    seen = set()
    prev = ''
    for car in t:
        for cur in car:
            if cur!=prev and cur in seen:
                return 0
            prev = cur
            seen.add(cur)
    return 1

def merge(car):
    seen = set()
    res = []
    prev = ''
    for c in car:
        if c not in seen:
            res.append(c)
            seen.add(c)
        elif c != prev:
            res.append(c)
        prev = c
    return ''.join(res)
    

for TC in range(1,int(input())+1):

    N = int(input())
    cars = tuple(map(merge, input().split()))

    print('Case #%d:' % TC, sum(map(valid, permutations(cars))))
