f=open('A-small-attempt0.in')
g=open('Result.in','w')
T=int(f.readline())
for i in range(T):
    fa=int(f.readline())
    fs=[]
    for _ in range(4):
        fs.append(map(int,f.readline().split()))
    sa=int(f.readline())
    ss=[]
    for _ in range(4):
        ss.append(map(int,f.readline().split()))
    if len(set(fs[fa-1]).intersection(set(ss[sa-1])))==0:
        g.write('Case #'+str(i+1)+': Volunteer cheated!\n')
    elif len(set(fs[fa-1]).intersection(set(ss[sa-1])))==1:
        t=list(set(fs[fa-1]).intersection(set(ss[sa-1])))
        g.write('Case #'+str(i+1)+': '+str(t[0])+'\n')
    else:
        g.write('Case #'+str(i+1)+': Bad Magician!\n')
g.close()
f.close()
