t=int(raw_input())
output=[]

for a0 in xrange(t):
    s,k=raw_input().split()
    k=int(k)
    s=list(s)
    v=len(s)
    n=0
    while ('-' in s ) and (s.index('-')<=v-k):
        j=s.index('-')
        for i in xrange(k):
            if s[j+i]=='-':
                s[j+i]='+'
            else :
                s[i+j]='-'
        n=n+1
    
    if '-' not in s :
        output.append(str(n))
    else :
        
        output.append('IMPOSSIBLE')
    
for a0 in xrange(t):
    print 'Case #'+str(a0+1)+': '+output[a0]
                       
                
