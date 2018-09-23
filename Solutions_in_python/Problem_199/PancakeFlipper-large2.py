
fout = open('PancakeFlipper-largegcj.out', 'w')

def lp(s, n):
    return (n-len(s))*'0'+s

def doprint(s):
    print(s)
    fout.write(s+'\n')

def close():
    fout.close()

T = int(input())
for tc in range(1, T+1):
    S, K_t = input().split()
    K = int(K_t)
    N = len(S)

    dic = {'-':-1, '+':1}
    v = [dic[S[i]] for i in range(len(S))]

    flips = 0 # why is this not sufficent?

    #flist = []

    dep = 0

    depchange = [0 for i in range(len(S))] # [bool]

    works = True

    for i in range(N):
            
    
        if v[i] == -1 and dep % 2 == 0 or v[i] == 1 and dep % 2 == 1:
            if i <= N-K: # < or <=?
                flips += 1
                dep += 1
                depchange[i+K-1] = 1 # the change occurs between i+K-1 and i+K
            else:
                #print('Fail', i)
                works = False

        if depchange[i]:
            dep -= 1 # NOT dep = 0

    assert dep == 0

    #print(v)
    #ansB = all(v[i] == 1 for i in range(len(v)))
    
    if not works:
        ans = "IMPOSSIBLE"
    else:
        ans = str(flips)           
    
    #print(flips)
    flips = 0
    doprint("Case #"+str(tc)+": "+str(ans))

close()

'''
6
---+-++- 3
+++++ 4
-+-+- 4
-+-+- 3
--- 3
++-----+-- 3
'''
