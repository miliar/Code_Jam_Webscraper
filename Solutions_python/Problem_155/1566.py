f=open('A-large.in')
g=open('Result.in','w')
T=int(f.readline())
for i in range(T):
    Smax,s=f.readline().split()
    standing=int(s[0])
    audience_needed=0
    for j in range(1,int(Smax)+1):
        if s[j]!='0':
            if standing<j:
                to_add=j-standing
                audience_needed+=to_add
                standing+=to_add+int(s[j])
            else:
                standing+=int(s[j])
    g.write('Case #'+str(i+1)+': '+str(audience_needed)+'\n')
g.close()
f.close()
