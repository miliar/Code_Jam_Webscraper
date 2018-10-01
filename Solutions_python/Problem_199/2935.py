
# coding: utf-8

# In[53]:

import pandas as pd
import numpy as np

df=pd.read_csv("A-large.in",skiprows=1,sep=" ",header=None)
df["case"]=df.index.map(lambda x: x+1)

d={'+':1,'-':0}

def to_01_array(s):
    return np.array([d[l] for l in list(s)])

def check_possible(l,k,case):
    turnlist=[]
    for step in range(len(l)-k+1):
        if l[step]!=1:
            l[step:(step+k)]=(l[step:(step+k)]+1)%2
            turnlist.append(1)
        else:
            turnlist.append(0)
    if l[step:(step+k)].all():
        return "Case #"+str(case)+": "+str(np.sum(turnlist))
    else:
        return "Case #"+str(case)+": IMPOSSIBLE"

f=open("pancakes_output","w")
f.write("\n".join(df.apply(lambda row: check_possible(to_01_array(row[0]),row[1],row["case"]),axis=1).tolist()))
f.close()

