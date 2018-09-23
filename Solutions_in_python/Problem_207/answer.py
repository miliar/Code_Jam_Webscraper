fi = open('input.in','r')
wa = open('output.out','w')
test = int(fi.readline())
for i in range(1,test+1):
    ans = ""
    a = list(map(int,fi.readline().split()))
    n = a[0]
    b = [[a[1],'R'],[a[3],'Y'],[a[5],'B']]
    b.sort(reverse=True)
    a = b[0][1]
    ans+=b[0][1]
    b[0][0]-=1
    while b[0][0]>0 or b[1][0]>0 or  b[2][0]>0:
        b.sort(reverse=True)
        j=0
        if a==b[j][1]:
            j+=1
        if b[j][0]==0:
            ans="IMPOSSIBLE"
            break
        a = b[j][1]
        ans+=b[j][1]
        b[j][0]-=1
    if ans!="IMPOSSIBLE" and ans[0]==ans[-1]:
        if ans[-1]!=ans[-3]:
            ans = ans[:-2] + ans[-1]+ans[-2]
        else:
            ans="IMPOSSIBLE"
        #print(str(i) +' '+ ans)
    #print('Case #{}: {}\n'.format(i,ans))
    wa.write('Case #{}: {}\n'.format(i,ans))
fi.close()
wa.close()

