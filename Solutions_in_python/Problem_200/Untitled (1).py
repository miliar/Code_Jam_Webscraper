
# coding: utf-8

# In[19]:


f = open('./B-small-attempt1.in', 'r')
ds = f.read()
#print ds
p = []
p = ds.split()
len(p)
t = int(p[0])


# In[20]:

def func1(n):
    c = n%10
    div = n/10
    b = div%10
    fin = div/10
    a = fin%10
    fout = fin/10
    d = fout%10
    return d,a,b,c


# In[21]:

l = []
#t = int(raw_input())
for i in range(t):
    n = int(p[i+1])
    l.append(n)
for i in range(t):
    n = l[i]
    d,a,b,c = func1(n)
    while(b>c):
        n = n-1
        d,a,b,c = func1(n)
    while(a>b):
        n= n-1
        d,a,b,c = func1(n)
    while(d>a):
        n= n-1
        d,a,b,c = func1(n)
   
    print 'Case #%d'%(i+1),':',n


# In[ ]:




# In[ ]:



