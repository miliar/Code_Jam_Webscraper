fr = open("input1.in", "r")
fw = open("output1.txt", "w")
t=int(fr.readline())
#t=int(input())
for i in range(t):
    m,n=fr.readline().strip().split()
    #m,n=input().split()
    n=int(n)
    s=[]
    sapp=s.append
    for j in m:
        if(j=="+"):
            sapp("1")
        else:
            sapp("0")
    l=len(s)
    count=0
    for j in range(l-n+1):
        if(s[j]=="0"):
            for k in range(j,j+n):
                #print(k,s)
                if(s[k]=="0"):
                    s[k]="1"
                else:
                    s[k]="0"
            count+=1
            #print(k)
        r=l-j-1
        if(s[l-j-1]=="0"):
            for k in range((l-j-n),(l-j))[::-1]:
                #print(k,s)
                #print(l-j)
                if(s[k]=="0"):
                    s[k]="1"
                else:
                    s[k]="0"
            count+=1
            #print(k)
    #print(m,n)
    if(s.count("1")==l):
        #print("Case #"+str(i+1)+": "+str(count))
        fw.write("Case #"+str(i+1)+": "+str(count)+"\n")
    else:
        #print("Case #"+str(i+1)+": IMPOSSIBLE")
        fw.write("Case #"+str(i+1)+": IMPOSSIBLE\n")
    #fw.write("Case #"+str(i+1)+": "+str(count)+"\n")
fw.close()
fr.close()
