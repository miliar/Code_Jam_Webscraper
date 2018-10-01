t=int(raw_input())


def num(s,k):
    n=len(s)
    s1=[]
    for i in range(n):
        s1.append(s[i])
    i=0
    count=0
    #a=''
    while i < (n-k+1):
        if s1[i]=='-':
            count+=1
            for j in range(i,i+k):
                if s1[j]=='-':
                    s1[j] = '+'
                else:
                    s1[j] = '-'
        i+=1
    #for i in range(n-k,n):
    #    a = a + s[i]
    #print 's1:',s1,'count:',count
    flag=True
    for i in range(n):
        if s1[i] == '-':
            flag=False
    if flag == True:
        return count
    else:
        return 'IMPOSSIBLE'



for i in range(t):
    s,k=raw_input().strip().split()
    k = int(k)
    print "Case #{}: {}".format(i+1,num(s,k))
