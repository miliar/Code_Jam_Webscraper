import sys
sys.stdin = open('D-large.in')
sys.stdout = open('Dl.out', 'w')

T = int(input())

def war(N, K):
    for n in N:
        k = 0
        while True:
            if k >= len(K):
                break
            if K[k] > n:
                K.pop(k)
                break
            else:
                k += 1  
    return len(K)

def dwar(N, K):
    wins = 0
    for n in N:
        if n < K[0]:
            K.pop()
        else:
            wins+=1
            K.pop(0)
    return wins


for case in range(T):
    turns = int(input())
    N = [float(x) for x in input().split()]
    K = [float(x) for x in input().split()]
    N.sort()
    K.sort()
    #print(N)
    #print(K)
    print("Case #{}: {} {}".format(case+1,
                                dwar(N[:], K[:]),
                                war(N[:], K[:])))

sys.stdout.close()
