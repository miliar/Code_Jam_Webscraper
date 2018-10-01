import string

ifile = open("B-large.in")
fs = ifile.read().split("\n")
ifile.close()

C = int(fs[0])

out = []

NKidx = 1
for c in range(0,C): 
    N = int(fs[NKidx].split(" ")[0])
    K = int(fs[NKidx].split(" ")[1])
    B = int(fs[NKidx].split(" ")[2])
    T = int(fs[NKidx].split(" ")[3])
    
    #get chickens (init,v,succ)
    ck = []
    ilist = fs[NKidx+1].split(" ")
    vlist = fs[NKidx+2].split(" ")
    for i in range(0,N):
        #print [int(ilist[i]), int(vlist[i]), (T*int(vlist[i])+int(ilist[i]) >= B)]
        ck.append( [int(ilist[i]), int(vlist[i]), (T*int(vlist[i])+int(ilist[i]) >= B)] )

    succ=0
    s_c=0
    s_w=0
    for i in range(N-1,-1,-1):
        if succ>=K:
            res = str(s_c)
            break;

        if ck[i][2]:#succ chick
            s_c += s_w
            succ+=1
        else:
            s_w+=1

    if succ>=K:
        res = str(s_c)
    else:
        res = "IMPOSSIBLE"

    out.append("Case #"+str(c+1)+": "+res)
    NKidx+=3

ofile = open("output.txt","w")
ofile.write(string.join(out,"\n"))
ofile.close()