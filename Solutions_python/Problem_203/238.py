filename ="A-large.in"
f= open(filename,'r')
out = open("output.txt",'w')
Cases= int(f.readline())
for T in range(Cases):
    [R,C]= [int (j) for j in f.readline().split(" ")]
    S=[[c for c in f.readline().rstrip()] for i in range(R)]
    #print([R,C])
    #print(S)
    #First fill it horizontally
    for r in S:
        lastc ="?"
        for i in range(len(r)+1):
            if i==len(r) or r[i]!="?":
                if i<len(r):
                    lastc=r[i]
                for j in range(i-1,-1,-1):
                    if r[j]=='?':
                        r[j]=lastc
                    else:
                        break
    for i in range(len(S)+1):
        if i==len(S) or S[i][0]!="?":
            if i<len(S):
                lastc=S[i]
            for j in range(i-1,-1,-1):
                if S[j][0]=='?':
                    S[j]=lastc
                else:
                    break
    print(S)
    ret="\n".join([''.join(r) for r in S])
    ret="Case #"+str(T+1)+": "+"\n"+ret
    print(ret)
    out.write(ret+"\n")
f.close()
out.close()
