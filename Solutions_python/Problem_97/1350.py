import math


n=[[],[],[],[],[],[],[]]
m=[[],[],[],[],[],[],[]]

def demo():
    a=open("Cbig.in")
    b=a.readlines()
    outf=open("Cext.txt","w")
    
    for i in range(int(b[0])):
        c=b[i+1].split(" ")
        min=int(c[0])
        max=int(c[1])
        
        res=0
        
        d=len(c[0])-1
        #print d

        for j in range(len(n[d])):
            if n[d][j]>=min and n[d][j]<=max and m[d][j]<=max:
                res+=1
                
        print "Case #"+str(i+1)+": "+str(res)
        outf.write("Case #"+str(i+1)+": "+str(res)+"\n")
    outf.close()


for leng in range(1,8):
    min=int(math.pow(10,leng-1))
    max=int(math.pow(10,leng))-1
    if leng==7:
        max=2000000
    print min,max
    
    if min>0:
        for j in range(min,max+1):
            d=str(j)
            g=[]
            for k in range(len(d)):
                e=d[k:len(d)]+d[0:k]
                f=int(e)
                if f not in g:
                    g.append(f)
            for f in g: 
                if j<f and f<=max:
                    n[leng-1].append(j)
                    m[leng-1].append(f)

raw_input("Got data?")
demo()

