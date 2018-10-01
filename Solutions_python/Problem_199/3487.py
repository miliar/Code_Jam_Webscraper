import sys

def flip(cakes, k, index):
    for x in range(k):
        if cakes[index + x] == '-':
            cakes[index + x] = '+'
        else:
            cakes[index + x] = '-'


def flips(cakes, k):
    ret = 0
    index = 0
    while(index <= len(cakes) - k):
        if(cakes[index] == '-'):
            flip(cakes, k, index)
            ret += 1
        index += 1
    for x in cakes:
        if x == '-':
            ret = "IMPOSSIBLE"
    return ret

n = int(sys.stdin.readline())
for i in range(n):
    cakes, k = sys.stdin.readline().split()
    cakes = list(cakes)
    k = int(k)
    print("Case #" + str(i + 1) + ": " + str(flips(cakes, k)))
