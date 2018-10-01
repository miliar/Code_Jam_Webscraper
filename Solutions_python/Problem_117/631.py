import math

def demo():
    a=open("B.in")
    b=a.readlines()
    outf=open("out.txt","w")
    
    lastLine=1
    
    for i in range(int(b[0])):
        N,M=b[lastLine].split(" ")
        data = []
        for j in range(int(N)):
            data.append(map(int,b[lastLine+j+1][:-1].split(" ")))
        lastLine+=1+int(N)
        
        res=check(N,M,data)
                
        print "Case #"+str(i+1)+": "+str(res)
        outf.write("Case #"+str(i+1)+": "+str(res)+"\n")
    outf.close()


def check(N,M,data):
    rotateData=zip(*data)
    for i in range(int(N)):
        for j in range(int(M)):
            if data[i][j]==1 and not(data[i].count(2)==0 or rotateData[j].count(2)==0):
                return "NO"
    return "YES"


raw_input("Got data?")
demo()