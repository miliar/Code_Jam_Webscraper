import math

tc = int(input())
for t in range(tc):
    n, k = map(int, input().split())

    closestpow = 2**int(math.log(k, 2))
    div = [int((n-(closestpow-1))/closestpow), math.ceil((n-(closestpow-1))/closestpow)]

    cutoff = (n-closestpow+1)/closestpow
    cutoff -= int((n-closestpow+1)/closestpow)
    cutoff *= closestpow
    cutoff += closestpow
    
    if k < cutoff:
        ans = [int((div[1]-1)/2), math.ceil((div[1]-1)/2)]
    else:
        ans = [int((div[0]-1)/2), math.ceil((div[0]-1)/2)]

    print('Case #'+str(t+1)+': ' + str(max(ans)), str(min(ans)))    
