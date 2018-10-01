x=['ejp mysljylc kd kxveddknmc re jsicpdrysi',
   'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
   'de kr kd eoya kw aej tysr re ujdr lkgc jv']
y=['our language is impossible to understand',
   'there are twenty six factorial possibilities',
   'so it is okay if you want to just give up']

d={}
d['q']='z'
d['z']='q'
for i in range(len(x)):
    for j in range(len(x[0])):
        if(x[i][j]!=' '):
            d[x[i][j]]=y[i][j]

if __name__ == '__main__':
    f=open('A-small-attempt0.in','r')
    data=f.readlines()
    f.close()
    t=int(data[0])
    f=open('out.txt','w')
    for i in range(t):
        z=data[i+1]
        f.write('Case #%d: '%(i+1))
        f.write(''.join(map(lambda x:d[x] if x.isalpha() else x,z)))
    f.close()
