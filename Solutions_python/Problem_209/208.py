import sys
import math

# surface : Pi*R**2
# perimeter : 2 * Pi * R * H

def greedy(pancakes,n,k):
    pancakes = sorted(pancakes,key=lambda x:-x[0])
    maxS = 0
    # print(n-k)
    for i in range(n-k+1):
        t = pancakes[i]
        hp = sorted(pancakes[(i+1):],key=lambda x:-(x[1]*x[0]))[:(k-1)]
        s = (t[0]**2)+2*t[1]*t[0]
        for j in range(k-1):
            s+=2*hp[j][1]*hp[j][0]
        maxS = max(maxS,s)
    return maxS


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    line = [int(x) for x in input().split()]
    N,K = line[0],line[1]
    pancakes = []
    for j in range(N):
        pancakes.append([int(x) for x in input().split()])
    res = greedy(pancakes,N,K)*math.pi

    # res = 0
    print("Case #{}: {}".format(i, res))
    # print(i, file=sys.stderr) #DEBUG
