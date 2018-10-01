import math as mt
import itertools as it
import numpy as np
import heapq as hq


def readint(f_in): return int(f_in.readline()[:-1])
def readfloat(f_in): return float(f_in.readline()[:-1])
def read_l(f_in): return f_in.readline()[:-1].split(' ')
def readint_l(f_in): return map(int,f_in.readline()[:-1].split(' '))
def readfloat_l(f_in): return map(float,f_in.readline()[:-1].split(' '))
def readchar_l(f_in): return list(f_in.readline()[:-1])
def plus_min_str_to10_l(str): return map(int,list(str.replace('+','1').replace('-','0')))
def list_to_str(out_list): return ' '.join(map(str,out_list))
def binarize(x,n): return  bin(x)[2:].zfill(n) #x - int, n - bits returns list
imp="IMPOSSIBLE"
pos="POSSIBLE"
inf=float('inf')
minf=(-1)*inf
pi=mt.pi
eps=10**(-9)
check_out=False
#check_out=True

f_in=open('in.in','r')
if (check_out):
    f_out = open('check.txt', 'w')
else:
    f_out=open('out.txt','w')


output=""
T=readint(f_in)

for test in range (T):
    output+="Case #"+str(test+1)+": "
    print "test: "+str(test+1)
    [n,p]=readint_l(f_in)
    g=readint_l(f_in)
    g=[g[i]%p for i in range (n)]
    s=[g.count(i) for i in range(p)]
    #res is no getters
    if p==2:
        res=s[1]/2
    else:
        if p==3:
            mi=min(s[1],s[2])
            su=max(s[1],s[2])-mi
            res=mi
            for i in range (su):
                if (i%3!=0):
                    res+=1
        else:
            if p==4:
                mi = min(s[1], s[3])
                su = max(s[1], s[3]) - mi
                res=mi+s[2]/2
                if (s[2]%2)==1:
                    start=2
                else:
                    start=0
                for i in range(start,su):
                    if (i % 4 != 0):
                        res += 1

    output+=str(n-res)+"\n"

if (check_out):
    f_check=open('out.txt','r')
    right_str=f_check.read()
    print right_str==output


f_out.write(output)
f_out.close()
f_in.close()



