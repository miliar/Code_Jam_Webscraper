from operator import itemgetter
from math import pi

def solve():
    n, k = map(int, input().split())
    cakes = [list(map(int, input().split())) for _ in range(n)]
    index = 0
    for cake in cakes:
        cake.append(2 * pi * cake[0] * cake[1])
        cake.append(index)
        index += 1
    
    highest = sorted(cakes, key=itemgetter(2), reverse=True)
    result = 0
    for cake in cakes:
        area = pi * cake[0] * cake[0] + cake[2]
        count = 1
        for c in highest:
            if count == k:
                result = max(result, area)
                break
            if c[0] <= cake[0] and c[3] != cake[3]:
                count += 1
                area += c[2]
        if count == k:
            result = max(result, area)

    return result


for t in range(int(input())):
    print('Case #%d: %r' % (t + 1, solve()))