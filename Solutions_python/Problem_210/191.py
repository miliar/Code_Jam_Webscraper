from  math import *
T = int(input())
for t in range(1,T+1):
    n, k = map(int,input().split())
    ac = [] 
    for i in range(n):
        r, h = map(int,input().split())
        ac.append((r,h))
    aj = [] 
    ac.sort()
    
    for i in range(k):
        r, h = map(int,input().split())
        aj.append((r,h))
    ans = 0  
    aj.sort()
    if n == 0 and k == 1 or n == 1 and k == 0:
            ans = 2
    elif n == 0:
        if aj[1][1] - aj[0][0] <= 720:
            ans = 2
        elif aj[0][1] + 1440 - aj[1][0] <= 720:
            ans = 2
        else: ans = 4
    elif k == 0:
        if ac[1][1] - ac[0][0] <= 720:
                ans = 2
        elif ac[0][1] + 1440 - ac[1][0] <= 720:
                ans = 2
        else: ans = 4        
    else:
        if ac[0][0] < aj[0][0]:
            if aj[0][0] - ac[0][0] >= 720 or ac[0][0] + 1440 - aj[0][0] >= 720:
                ans = 2
            else: ans = 4
        else:
            if ac[0][0] - aj[0][0] >= 720 or aj[0][0] + 1440 - ac[0][0] >= 720:
                ans = 2
            else: ans = 4            
    print('Case #'+str(t)+':', ans)
        