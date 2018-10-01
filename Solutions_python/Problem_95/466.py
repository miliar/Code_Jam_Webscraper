def solve(text):
    x=['our language is impossible to understand','there are twenty six factorial possibilities','so it is okay if you want to just give up','a zoo','q']
    y=['ejp mysljylc kd kxveddknmc re jsicpdrysi','rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd','de kr kd eoya kw aej tysr re ujdr lkgc jv','y qee','z']
    d=dict()
    for i in range(len(x)):
        for j in range(len(x[i])):
            d[y[i][j]]=x[i][j]
    r=''
    for c in text:
        r+=d[c]
    return r

finput='googlerese.in'
foutput='googlerese.out'

ifile=open(finput,"r")
ofile=open(foutput,"w")

T=int(ifile.readline().strip('\n'))
for i in range(T):
    line=ifile.readline().strip('\n')
    r=solve(line)
    
    print('Case #'+str(i+1)+':',r,file=ofile)
    print('Case #'+str(i+1)+':',r)

ifile.close()
ofile.close()
