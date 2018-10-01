import sys
n = int(input())

for i in range(n):
    # i=+1
    d={}
    s,k=input().split()
    s=list(s)
    for j in range(len(s)):
        d[j]=s[j]
    # print(d)
    c=0
    for j in range(len(d)):
        imp=False
        # d[j]=s[j]
        if d[j]!='-':
            pass
        else:
            for x in range(int(k)):
                # print(x)
                try:
                    if d[j+x]=='+':
                        d[j+x]='-'
                        # c+=1
                    else:
                        d[j+x]='+'
                except:
                    imp=True
                    print("Case #{0}: {1}".format(i+1, 'IMPOSSIBLE'))
                    break
                    print('Hi')
            if imp==True:
                break
            c+=1
    if imp==False:
        print("Case #{0}: {1}".format(i+1, c))
