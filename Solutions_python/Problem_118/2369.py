import math
fname='C-small-attempt2'
file=open(fname+'.in','r').read().splitlines();
out=open(fname+'.out','w')
T=int(file[0]); file=file[1:T+1];
limit=1000
case=1
q=math.sqrt
o=[]

def pd(x,y):
    v=range(x,y+1);arr=[];pds=[]
    for i in v:
        if i==int(str(i)[::-1]):
            arr.append(i)
            if q(i)==int(q(i)):
                if int(q(i))==int(str(int(q(i)))[::-1]):
                    pds.append(i)
    return str(len(pds))

for x in file:
    z=x.split(' ')
    a=int(z[0]);b=int(z[1])
    pds = pd(a,b) if 1<=a<=b<=limit else '0'
    o.append('Case #'+str(case)+': '+pds+'\n')
    case+=1

for x in o:
    out.write(x)
out.close()
