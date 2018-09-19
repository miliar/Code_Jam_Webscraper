#Python 2.6.2 Windows XP
#Google Code Jam 2009
#Jonathan Hsu

#Welcome to Code Jam
#suffix tree desperately needed, recursive walk of position table

import os,glob

foo = "welcome to code jam"

for fname in glob.glob("*.in"):
    if(os.path.exists(fname.replace(".in",".out"))): continue
    
    f = open(fname)
    fo = open(fname.replace(".in",".out"),"w+")

    
    n = int(f.readline())
    ans=[]
    for iii in range(n):
        inp=f.readline()

        tbl1=[[] for i in foo]
        #tbl2=[[] for i in foo]
        for i,iv in enumerate(inp):
            for j,jv in enumerate(foo):
                if(iv==jv):
                    tbl1[j].append(i)
                    #tbl2[j].append(i)

        #stk=[0 for i in foo]
        
        #s=" ".join(["for x%d in tbl1[%d]"%(i,i) for i in range(len(foo))])
        #s1="<".join(["tbl1[%d][0]"%i for i in range(len(foo))])

        global cnt
        cnt=0
        def walk(x):
            global cnt
            if(len(x)==len(foo)):
                cnt+=1
                if(cnt==1000):
                    cnt=0
                return
            for i in tbl1[len(x)]:
                if(x[-1]<i):
                    walk(x[:]+[i])
                
        for i in tbl1[0]:
            walk([i])

        ans.append("Case #%d: %04d"%(iii+1,cnt%1000))

        
    fo.write("\r\n".join(ans))
    f.close()
    fo.close()


    
