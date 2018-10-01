import numpy as np
import math



def compare (item1, item2):
    fitness1 = item1[0]*item1[1]
    fitness2 = item2[0] * item2[1]
    if fitness1 < fitness2:
        return -1
    elif fitness1 > fitness2:
        return 1
    else:
        return 0

def fitness(item1):
    return item1[0]*item1[1]

input = open('task1.in','r')
output = open('output.txt','w+')
T = int(input.readline())

for t in range(T):
    points = []
    N, K = map(int, input.readline().split())
    R = [(0,0) for i in range (N)]
    H = np.zeros(N)
    for i in range(N):
        x, y = map(int, input.readline().split())
        R[i] = (x, y)
    R = sorted(R, key = fitness, reverse = True)

    maxsum = 0

    for i in range(N):
        sum = 2*math.pi*fitness(R[i]) + math.pi*R[i][0]*R[i][0]
        num = 1
        for j in range(N):
            if num == K:
                continue
            if R[j][0] <= R[i][0] and i != j:
                sum += 2*math.pi*fitness(R[j])
                num += 1
        if num == K and sum > maxsum:
            maxsum = sum

    output.write("Case #{}: {}\n".format(t + 1, maxsum))