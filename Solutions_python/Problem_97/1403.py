def sh(s):
    t = s[1:]+s[0]
    if t[0]!=0:
        return t
    return s


fin = open("bin", "r")
fout = open("bout","w")
cases = int(fin.readline())
for p in range(cases):
    A,B = [int(x) for x in fin.readline().split()]
    ans = 0
    d = dict()
    for k in range(A,B):
        t = sh(str(k))
        for i in range(len(str(A))-1):
            if(k<int(t)<=B) and len(str(k)) == len(str(int(t))) and A<=int(t) and k<int(t) and not d.has_key((k,int(t))):
                d[(k,int(t))]=1
                ans+=1
            t = sh(t)
    fout.write("Case #{0}: {1}\n".format(p+1,ans))
fin.close()
fout.close()