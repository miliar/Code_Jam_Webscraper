f1 = open("B-small-attempt3.in","r")
f2 = open("out.txt","w")

data = f1.readlines()
k = int((data[0].split())[0])
for ind in range(1,k+1):
    dim=data[ind].split()
    n=int(dim[0])
    r=int(dim[1])
    o=int(dim[2])
    y=int(dim[3])
    g=int(dim[4])
    b=int(dim[5])
    v=int(dim[6])
    if b<=o and o!=0 and n>b+o:
        f2.write("Case #"+str(ind)+": IMPOSSIBLE\n")
        continue
    if r<=g and g!=0 and n>r+g:
        f2.write("Case #"+str(ind)+": IMPOSSIBLE\n")
        continue
    if y<=v and v!=0 and n>y+v:
        f2.write("Case #"+str(ind)+": IMPOSSIBLE\n")
        continue
    R = "RG"*g+"R"
    Y = "YV"*v+"Y"
    B = "BO"*o+"B"
    r-=g
    y-=v
    b-=o
    if r>y+b or y>b+r or b>y+r:
        f2.write("Case #"+str(ind)+": IMPOSSIBLE\n")
        continue
    st=""
    somma=r+y+b
    while somma>1:
        if r==max(r,y,b):
            if y==max(y,b):
                st+="RY"
                r-=1
                y-=1
            else:
                st+="RB"
                r-=1
                b-=1
        elif y==max(r,y,b):
            if r==max(r,b):
                st+="YR"
                y-=1
                r-=1
            else:
                st+="YB"
                y-=1
                b-=1
        else:
            if r==max(r,y):
                st+="BR"
                b-=1
                r-=1
            else:
                st+="BY"
                b-=1
                y-=1
        somma-=2
    if r==1:
        st+="R"
    elif b==1:
        st+="B"
    elif y==1:
        st+="Y"
    ss = list(st)
    l = len(ss)
    corr = True
    if l>0 and ss[0]==ss[l-1]:
        corr = False
    i=l-1
    while corr==False:
        ss[i-1],ss[i]=ss[i],ss[i-1]
        i-=1
        if ss[i]!=ss[i-1]:
            corr=True
    if "R" in ss:
        ss[ss.index("R")]=R
    if "Y" in ss:
        ss[ss.index("Y")]=Y
    if "B" in ss:
        ss[ss.index("B")]=B
    f2.write("Case #"+str(ind)+": "+"".join(ss)+"\n")

f1.close()
f2.close()
