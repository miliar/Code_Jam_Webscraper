f1 = open('input.txt','r')
f2 = open('output.txt','w')
t = int(f1.readline())
for r in range(t):
    sp = f1.readline().strip().split(' ')
    st = sp[0]
    k = int(sp[1])
    ans = 0
    fl = [0]*len(st)
    n = len(st)
    for i in range(n-k+1):
        if st[i] == '-' and fl[i]%2 == 0:
            ans+=1
            for j in range(i,i+k):
                fl[j] +=1
        elif st[i] == '+' and fl[i]%2 != 0:
            ans += 1
            for j in range(i,i+k):
                fl[j]+=1
    flag = True
    for i in range(n):
        if st[i] == '-' and fl[i]%2 == 0:
            flag = False
            break
        elif st[i] == '+' and fl[i]%2 != 0:
            flag = False
            break
    if flag == True:
        wstr = 'Case #'+str(r+1)+': '+str(ans)+'\n'
        f2.write(wstr)
    else:
        wstr = 'Case #'+str(r+1)+': IMPOSSIBLE'+'\n'
        f2.write(wstr)
