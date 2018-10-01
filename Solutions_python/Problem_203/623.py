t = int(input())  # read a line with a single integer
for A in range(1, t + 1):
    r, c = [int(e) for e in input().split(" ")]
    G=[]
    for i in range(0,r):
        G.append(list(input()))
    Set=set()
    Set.add("?")
    for i in range(0,r):
        for j in range(0,c):
            m=j 
            M=j
            mr=i
            Mr=i 
            if (G[i][j] in Set):
                continue
            Set.add(G[i][j])
            while M+1<c and G[i][M+1]=="?":
                M+=1
                G[i][M]=G[i][j]
            while m-1>=0 and G[i][m-1]=="?":
                m-=1
                G[i][m]=G[i][j]
            while(True):
                mr-=1
                if mr<0 :
                    break
                b=False
                for a in range (m,M+1):
                    if G[mr][a]!="?":
                        b=True
                if b :
                    break
                for a in range (m,M+1):
                    G[mr][a]=G[i][j]
            while(True):
                Mr+=1
                if Mr>=r :
                    break
                b=False
                for a in range (m,M+1):
                    if G[Mr][a]!="?":
                        b=True
                if b :
                    break
                #print ("blah "+str(i)+" "+str(j)+" "+ G[i][j])
                for a in range (m,M+1):
                    #print (str(m)+" "+str(M)+" "+str(mr)+" "+str(Mr)+" "+str(a)+" "+G[Mr][a])
                    G[Mr][a]=G[i][j]
                
                
                
                
                
    print("Case #{}:".format(A))
    for a in range (0,r):
        print ("".join(G[a])) 
    print("")