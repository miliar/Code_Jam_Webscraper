from math import log

def mini(n):
    if n%2 != 0:
        return (n-1)//2
    else:
        return (n//2)-1

def maxi(n):
    if n%2 != 0:
        return (n-1)//2
    else:
        return n//2

def div(n, c):
    mx = maxi(n)
    mn = mini(n)
    return [[mx, c], [mn, c]]

def concat(A):
    red = list(set([a[0] for a in A]))
    red.sort()
    red.reverse()
    C = []
    for r in red:
        c = 0
        for a in A:
            if a[0] == r:
                c += a[1]
        C.append(c)
    ans = []
    for i in range(len(red)):
        ans.append([red[i], C[i]])
    return ans

def compute(N, K):
    red = [[N, 1]]
    lim = int(log(K, 2))
    i = 0
    while i != lim:
        A = []
        for r in red:
            n = r[0]
            c = r[1]
            A.extend(div(n,c))
        red = concat(A)
        i += 1
    S = K - 2**lim + 1
    if red[0][1] < S:
        return red[1][0]
    else:
        return red[0][0]

file = open('bath_med.txt')
ANS = open('bath_med_ans.txt','w')

T = int(file.readline())
for i in range(T):
    N, K = map(int, file.readline().split(' '))
    ans = compute(N, K)
    mx, mn = maxi(ans), mini(ans)
    a = str('Case #%d: %d %d\n'%(i+1, mx, mn))
    ANS.write(a)

"""
T = int(input())
for i in range(T):
    n, k = map(int, input().split(' '))
    ans = compute(n, k)
    print(maxi(ans), mini(ans))
"""

        
        
        
