f=open("plb.txt","r")
g=open("ans.txt","w+")
b=[]
a=int(f.readline())
ans=""
def checkbig(s):
    for i in range(len(s)):
        for j in range(i,len(s)):
            if(s[i]>s[j]):
                for k in range(i,j):
                    if(s[k]>s[i]):
                        return k
                return i
    return -1;
for i in range(a):
    b=f.readline()
    if(b[len(b)-1]=='\n'):
        b=b[:len(b)-1]
    c=checkbig(b)
    if(c==-1):
        print("Case #%d: %s" %((i+1),b))
    else:
        for x in range(c):
            ans=ans+b[x]
        t=int(b[c])-1
        ans=ans+str(t)
        for x in range(c,len(b)-1):
            ans=ans+str(9)
        if(ans[0]=="0"):
            ans=ans[1:]
        print("Case #%d: %s" %((i+1),ans))
    ans=""
        
            
        
