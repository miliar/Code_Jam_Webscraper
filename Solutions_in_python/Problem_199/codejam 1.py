def solve(s,i,k):

    for j in range(i,i+k):
        if s[j]=='-':
            s[j]='+'
        else:
            s[j]='-'




for a0 in range(int(input())):
    s,k=input().split(' ')
    k=int(k)
    count=0
    s=list(s)

    for i in range(len(s)-k+1):
        if s[i]=='+':
            continue
        count += 1
        solve(s,i,k)


    c=s.count('-')
    if c > 0:
        print('Case #{0}: IMPOSSIBLE'.format(a0+1))
    else:
        print("Case #{0}: {1}".format(a0+1, count))

