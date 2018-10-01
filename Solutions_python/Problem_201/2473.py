def solve(n,k):
    blank=[n]
    ret=[]
    if n==k:return (0,0)
    for _ in range(k):
        L=max(blank)
        Li=blank.index(L)
        if not L%2:tmp=[int(L/2)-1,int(L/2)]
        else:tmp=[int((L-1)/2),int((L+1)/2)-1]
        ret=tmp
        blank.remove(L)
        blank.insert(Li,tmp[0])
        blank.insert(Li+1,tmp[1])
    return max(ret),min(ret)

t=int(input())
for a in range(1,t+1):
    n,k=[int(x) for x in input().split()]
    l,s=solve(n,k)
    print('Case #{0}: {1} {2}'.format(a,l,s))
