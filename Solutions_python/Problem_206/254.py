T = int(input())
for t in range(1,T+1):
    d, n = map(int,input().split())
    h = []     
    for i in range(n):
        h.append(list(map(int,input().split())))
    h.sort(reverse = True)
    tt = (d-h[0][0])/h[0][1]    
    for hh in h:
        if (d-hh[0])/hh[1] > tt:
            tt = (d-hh[0])/hh[1]
    ans = d/tt
        
    print('Case #'+str(t)+':', ans)
        