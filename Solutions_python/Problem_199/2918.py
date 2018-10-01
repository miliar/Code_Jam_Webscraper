def opf(s,k):
    n=len(s)
    i,r=0,0
    while i<n-k+1:
        if s[i]=='-':
            for j in range(i,i+k):
                if s[j]=='-':
                    s[j]='+'
                else:
                    s[j]='-'
            r+=1
        #print s,i,r
        i=i+1
    
    if '-' in s[n-k:]:
        return "IMPOSSIBLE"
    else:
        return r

    


if __name__ == "__main__":
    n=int(raw_input())
    for e in range(1,n+1):
        d=raw_input().split()
        s=list(d[0])
        #print len(s)
        k=int(d[1])
        print "Case #%s: %s" %(e , opf(s,k))

