def isIncreasing(n):
    prev=10
    while n!=0:
        rem=n%10
        if prev < rem:
            return False
        prev=rem
        n/=10
    return True

def checkUptoIncreasing(N):
    N=str(N)
    for i in range(0,len(N)-1):
        if N[i]  > N[i+1]:
            return i



def checker(N):

    if isIncreasing(N):
        return N
    else:
        while not isIncreasing(N):
            upto=checkUptoIncreasing(N)
            N=str(N)
            make_zero=(len(N)-upto-1)
            N=N[0:upto+1]+ ('0' * make_zero)
            N=int(N)-1
        return N

T=int(input())
for idx in range(1,T+1):
    N=int(input())
    print 'Case #{}: {}'.format(idx,checker(N))
