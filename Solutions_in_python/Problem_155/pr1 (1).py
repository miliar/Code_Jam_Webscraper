
# coding: utf-8

# In[8]:

path1="E:\Downloads\A-large-attempt0.in"
f1=open(path1)
f2=open(path1.replace("in","out"),mode='w')
for j,line in enumerate(f1.readlines()):
    if j>0:
        #print line
        str1=line.split(' ')[1].strip()
        s=0
        a=0
        for i,d in enumerate(str1):
            d=int(d)
            if d==0 and s<i+1: 
                #print i, a, s
                d=1
                a+=1 
            s+=d
        f2.write("Case #{}: {}\n".format(j, a))
f1.close()
f2.close()


# In[ ]:



