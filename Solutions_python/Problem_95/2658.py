# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 07:33:27 2012

@author: m4chfr4m3
"""
"""i=0
gs=[]
while i<3:
    f=raw_input('enter in googlerese sample :-')
    gs.append(f)
    i=i+1
i=0
es=[]
while i<3:
    g=raw_input('enter the output in english :-')
    es.append(g)
    i=i+1
dic={}
for j in range(0,3):
    sl=gs[j]
    sll=es[j]
    for k in range(0,len(sl)):
        if sl[k] != ' ':
            if sl[k] in dic.keys():
                continue
            else:
                dic[sl[k]]=sll[k]"""
dic={'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}
print(dic)
dic['z']='q'
dic['q']='z'
global dic
def conv(n):
    n=str(n)    
    m=[]  
    r=''    
    for o in range(0,len(n)-1):
        if n[o] != ' ':
            m.append(dic[n[o]])
        else:
            m.append(' ')
    for p in range(0,len(m)):
        r = r + m[p]
    return(r)


f=open('input.in','r')
g=open('output.txt','w')
l=f.readlines()
for m in range(1,len(l)):
    q = 'Case #'+str(m)+': '+conv(l[m])
    g.write(q+'\n')
f.close()
g.close()