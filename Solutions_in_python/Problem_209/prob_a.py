
import math

def f(pancakes, k):
    sides = sorted([(i, 2*pancakes[i][0]*pancakes[i][1]) 
                    for i in range(len(pancakes))],
                   key=lambda x: -x[1])

    m = 0

    for i in range(len(pancakes)):
        m = max(m, pancakes[i][0]**2 + g(sides, k-1, i) +
                2*pancakes[i][0]*pancakes[i][1])
        
                
    return m*math.pi
        


def g(sides, k, e):
    x = 0
    i = 0
                
    while(k > 0):
        if sides[i][0] != e:
            k -= 1
            x += sides[i][1]

        i += 1
    
    return x
    


t = int(input())
for testCase in range(t):
    n, k = map(int, input().split())

    pancakes = []

    for i in range(n):
        r, h = map(int, input().split())
        pancakes.append((r, h))

    print('Case #' + str(testCase+1) + ':', '{0:.6f}'.format(f(pancakes, k)))
