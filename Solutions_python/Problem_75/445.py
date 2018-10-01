x='inp.txt'


with open(x,'r') as Z:
    i=Z.readlines()

t=int(i[0])
i=i[1:]
zds=[]
for s in i:
    z={'Q':[],'W':[],'E':[],'R':[],'A':[],'S':[],'D':[],'F':[]}
    comb={}
    s2=s.split()
    if s2==[]:break
    b=int(s2[0])
    for k in range(b):
        comb[s2[k+1][:2]]=s2[k+1][2]
        comb[s2[k+1][:2][::-1]]=s2[k+1][2]
    s2=s2[1+b:]
    d=int(s2[0])
    for k in range(d):
        z[s2[k+1][0]].append(s2[k+1][1])
        z[s2[k+1][1]].append(s2[k+1][0])
    s2=s2[1+d:]
    q=int(s2[0])
    q2=str(s2[1:][0])
    s=''
    #print(b,comb,d,z,q,q2)
    for var in q2:
        s+=var
        for variable in comb:
            e=comb[variable]
            s=s.replace(variable,e)
        #print(var,s[-1])
        if var==s[-1] and var in 'FDSAREWQ':
            for v in s:
               if v in z[var]:
                    s=''
    s=list(s)
    zds.append(s)

z_=open('out.txt','w')
for d in range(len(zds)):z_.write('Case #'+str(d+1)+': '+str(zds[d]).replace("\'",'')+'\n')
z_.close()

print('end')

