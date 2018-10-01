# from sortedcontainers import SortedList
import math
f = open('B-small-practice.in', 'r')
t = int(f.readline())

for tc in range(1, t + 1):
    maxt = -1
    print("Case #" + str(tc) + ": ", end = "")
    D, N = map(int, f.readline().strip().split())
    for i in range(N):
        K, S = map(int, f.readline().strip().split())
        temp = (D - K) / S
        maxt = max(maxt, temp)
    print(D / maxt)