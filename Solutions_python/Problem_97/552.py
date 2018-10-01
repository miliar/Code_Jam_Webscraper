#precomputing

import sys

def debug(s):
    sys.stderr.write(s + "\n")

def printf(s):
    debug(s)
    print s

def next(i):
    current = i
    leading0 = 0
    m = 10
    while current%10 == 0:
        leading0 +=1
        m *= 10
        current /= 10

    res = i / m
    mult = 1
    while mult <= res:
        mult *= 10
    res += mult * (i%m)
    return res

d = {}
for i in range(1, 2000000):
    current = i
    equiv = [i]
    while True:
        current = next(current)
        if current < i:
            break
        elif current == i:
            d[i] = equiv
            break
        equiv.append(current)
debug("finished precomputing the dict")

n = int(raw_input())

def solve(a, b, d):
    sum = 0
    for s in d.itervalues():
        n = len(filter(lambda x: a<=x<=b, s))
        sum += n*(n-1)/2
    return sum

for i in range(n):
    tab = map(int, raw_input().split(' '))
    printf("Case #" + str(i+1) + ": " + str(solve(tab[0], tab[1], d)))

