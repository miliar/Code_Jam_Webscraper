def flip(s,k):
    n=0
    if (s.find('-')==-1):
        return str(n)
    while (len(s)>=k):
        a=s.find('-')
        s1=s[a:]
        if (len(s1)<k):
            break
        s=s1[:k].replace('+','.').replace('-','+').replace('.','-')+s1[k:]
        n=n+1
        if (s.find('-')==-1):
            return str(n)
    return 'IMPOSSIBLE'


def pancake(file):
    f=open(file)
    g=open('output.ou',mode='w')
    b=int(f.readline()[:-1])
    for x in range(b):
        (s,k) = f.readline()[:-1].split(' ')
        k = int(k)
        c=flip(s,k)
        g.write("Case #"+str(x+1)+": "+str(c)+"\n")
    f.close()
    g.close()
