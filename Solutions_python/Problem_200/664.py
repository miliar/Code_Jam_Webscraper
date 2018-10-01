import sys
import time

def read(f = int): return f(input())
def readlist(f = int): return list(map(f, input().split()))
def printd(msg): print(msg); print(msg, file=sys.stderr)

def solve():
    N = read(str)
    for i in range(1,len(N)):
        if N[i]<N[i-1]:
            for j in range(i-1,0,-1):
                if N[j]>N[j-1]:
                    return N[0:j] + str(int(N[j])-1) + '9'*(len(N)-j-1)
            return int(str(int(N[0])-1) + '9'*(len(N)-1))
    return N

start = time.clock()
for t in range(read()):
    printd('Case #{}: {}'.format(t+1, solve()))
print(time.clock()-start, file=sys.stderr)
