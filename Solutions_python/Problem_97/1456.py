import re
def genrecycled(n):
    s= str(n)
    res=[]
    for i in range(1,len(s)):
        res.append(int(s[i:] + s[:i]))
    return res
fname='C-small-attempt0.in'
fin=open(fname)
fout=open(fname+".out.txt", "w")
T = int(fin.readline().strip())
for ti in range(T):
    dictio={}
    splitter = re.compile(r'[\D]') # Match non-digits
    data_list = map(int,splitter.split(fin.readline().strip()))
    a=data_list[0];
    b=data_list[1]
    #print a,b
    for x in range(b-a):
        n=a+x
        m=genrecycled(n)
        for mi in m:
            if a<=n<mi<=b:
                dictio[(n,mi)]=1
    fout.write("Case #{0}: {1}\n".format( ti+1, len(dictio)))
fin.close()
fout.close()
