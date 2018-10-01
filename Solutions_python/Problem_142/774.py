# -*- coding: utf-8 -*-
"""
Created on Sat May 03 17:57:42 2014

@author: Matthieu
"""

def dec(l):
    curr = l[0]
    nomb = 0
    li = []
    for car in l:
        if car==curr:
            nomb += 1
        else:
            li.append((curr,nomb))
            curr = car
            nomb = 1
    li.append((curr,nomb))
    return li
    
def inti(f):
    u = int(f)
    if abs(f-u)>0.5:
        return u+1
    else:
        return u
    
inp = open("input2.in","r")
out = open("output","w")
T =  int(inp.readline())

for t in range(T):
    out.write("Case #"+str(t+1)+": ")
    N = int(inp.readline())
    st = []
    for _ in range(N):
        st.append(inp.readline())
    st2 = map(dec,st)
    l = len(st2[0])
    c= False
    mean = [0 for i in range(len(st2[0]))]
    for i in st2:
        if len(i)!=l:
            out.write("Fegla Won")
            c = True
            break
        for (ind,j) in enumerate(i):
            if j[0]!= st2[0][ind][0]:
                out.write("Fegla Won")
                c = True
                break
            mean[ind]+=j[1]
    if c:
        out.write("\n")
        continue
    mean = [inti(round(i/(1.0*len(st2)))) for i in mean]
    sums = [0 for i in range(len(mean))]
    for i in st2:
        for (ind,j) in enumerate(i):
            sums[ind]+=abs(mean[ind]-j[1])
    s = sum(sums)
    out.write(str(s)+ "\n")
    
        
    

out.close()
    
    


