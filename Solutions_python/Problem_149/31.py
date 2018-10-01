import sys
from bisect import bisect
f=open("input" if len(sys.argv)<2 else sys.argv[1])
T=int(f.readline())


def best(A):    
    
    rtn = 0        
    while A:
        #print("A=", A)
        #print(list((a,i) for i,a in enumerate(A)))
        a,i = min((a,i) for i,a in enumerate(A))
        #print((a,i))
        right = len(A)-1
        if i <= right -i:
            rtn += i
        else:
            rtn += right - i
        A = A[:i]+A[i+1:]
    return rtn
        


for t in range(1, T+1):
    N = int(f.readline())
    A = list(map(int, f.readline().split()))
    
    #print(t, N, X, S)
    print("Case #%d: %d"%(t, best(A)))
