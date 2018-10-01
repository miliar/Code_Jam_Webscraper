import queue
import math
Tmax = int(input())
t = 0
while t < Tmax:
    t += 1
    q = queue.PriorityQueue()
    n, k = list(map(int,input().split()))
    q.put(-n)
    r = 0
    for i in range(k):
        r = -q.get() - 1
        a = (math.ceil((r)/2))
        b = (int(r/2))
    
        q.put(-a)
        q.put(-b)
    print("Case #{}: {} {}".format(t, a, b))

