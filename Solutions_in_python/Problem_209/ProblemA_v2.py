import math
import itertools

def side(r, h):
    return 2 * math.pi * r * h

def area(r):
    return math.pi * r**2

t = int(raw_input().strip())
for ti in range(1, t+1):
    max_answer = 0
    radii = []
    sides = []
    n,k = [int(x) for x in raw_input().strip().split(' ')]
    for ni in range(n):
        r,h = [int(x) for x in raw_input().strip().split(' ')]
        side_area = side(r, h)
        radii.append(r)
        sides.append(side_area)
    for combo in itertools.combinations(range(n), k):
        total = 0
        max_r = 0
        for i in combo:
           if radii[i] > max_r:
               max_r = radii[i]
           total += sides[i]
        total += area(max_r)
        if total > max_answer:
            max_answer = total            
    answer = '{:.10f}'.format(max_answer)
    print 'Case #' + str(ti) + ': ' + str(answer)