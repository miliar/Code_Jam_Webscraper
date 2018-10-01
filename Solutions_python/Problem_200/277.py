def tidy(s):    
    if len(s)==1:
        return s
    N=len(s)
    #print s,N
    pos=0
    pos2=0
    for i in range(1,N):
        if int(s[i])>int(s[i-1]):
            pos=i
            pos2=i
        elif int(s[i])==int(s[i-1]):
            pos2=i
        elif int(s[i])<int(s[i-1]):
            break
        
    if pos2==N-1:
        return s
        
    if pos==0:
        if s[0]=='1':
            return '9'*(N-1)
        else:
            return str(int(s[0])-1)+'9'*(N-1)
    else:
        return s[:pos]+str(int(s[pos])-1)+'9'*(N-pos-1)
    

out=open("out.txt","w")
with open("B-large.in") as file: #A-large.in
    T=int(file.readline())
    #print T
    for case in range(T):
        s=file.readline().rstrip()
        ans=tidy(s)
        print ans
        out.write("Case #"+str(case+1)+": "+ans+"\n")
out.close()