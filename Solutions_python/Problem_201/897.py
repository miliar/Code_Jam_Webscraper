import math

def readint(f_in): return int(f_in.readline()[:-1])
def readfloat(f_in): return float(f_in.readline()[:-1])
def read_l(f_in): return f_in.readline()[:-1].split(' ')
def readint_l(f_in): return map(int,f_in.readline()[:-1].split(' '))
def readfloat_l(f_in): return map(float,f_in.readline()[:-1].split(' '))
def readchar_l(f_in): return list(f_in.readline()[:-1])
def plus_min_str_to10_l(str): return map(int,list(str.replace('+','1').replace('-','0')))
def list_to_str(out_list): return ' '.join(map(str,out_list))
imp="IMPOSSIBLE"

f_in=open('in.txt','r')
f_out=open('out.txt','w')
output=""
T=readint(f_in)

def add_to_dict(d,i,n):
    if (d.has_key(i)):
        d[i]+=n
    else:
        d[i]=n
for i in range (T):
    output+="Case #"+str(i+1)+": "
    row=readint_l(f_in)
    n=row[0]
    k=row[1]
    bs=len(bin(k)[2:])
    d={}
    d[n]=1
    dnew={}
    for i in range(bs-1):
        dnew={}
        for i in d.iterkeys():
            add_to_dict(dnew,math.ceil((i-1)/2.0),d[i])
            add_to_dict(dnew, math.floor((i - 1) / 2.0), d[i])
        d=dnew
    keys=d.keys()
    if(k-(2**(bs-1)-1)<=d[max(keys)]):
        out=max(keys)
    else:
        out = min(keys)
    out_list=[int(math.ceil((out-1)/2.0)),int(math.floor((out-1)/2.0))]
    output+=list_to_str(out_list)
    output+="\n"

f_out.write(output)
f_out.close()
f_in.close()
