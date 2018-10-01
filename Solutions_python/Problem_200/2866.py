def ans(n):
    ind=0
    lenN=len(n)
    flag=True
    for x in xrange(lenN):
        if n[ind]<n[x]:
            ind=x
        if n[x]<n[x-1] and x!=0:
            flag=False
            break
       
    if flag:
        res=''
        for x in n:
            if x!='0':
                res+=x
        return res
    else:
        n[ind]=int(n[ind])
        n[ind]-=1
        n[ind]=str(n[ind])
        
        for x in xrange(ind+1, lenN):
            n[x]='9'
        res=''
        
        for x in n:
            if x!='0':
                res+=x

        return res
            
        
with open ('in.txt') as ifile:
    inp = ifile.readlines()

wfile=open('out.txt', 'w')

t=int(inp[0])
for x in xrange(t):
    res='Case #'+str(x+1)+': '
    n=list(str(int(inp[x+1])))
    wfile.write(res+ans(n)+'\n')
          
wfile.close()
