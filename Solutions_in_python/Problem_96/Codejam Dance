out=[]    
def runin(s):
    count=0
    s=s.split()
    man = int(s[0])
    surprise=int(s[1])
    bound = int(s[2])
    i=0
    while(i<man):
        
        y=int(s[3+i])
        if y<=(3*bound):
            if y!=0 and y<=30:
                y=y-bound
                y=y/2
                if(y+1 >=bound):
            
                    count=count+1
                elif(y+2>=bound and surprise>0):
            
                    count=count+1
                    surprise=surprise-1
            elif y==0:
                if bound==0:
                    count=count+1
            
        else:
            count=count+1
        i=i+1
    return count
def write(out):
    r=open("C:\Users\SJ\Downloads\Cj2.out",'w')
    for i in out:
        r.write(i)

r = open("C:\Users\SJ\Downloads\B-large.in","r")
n = int(r.readline())
print n
for i in range(1,n+1):
    a=r.readline()
    print "Q case #"+str(i)+":"+a
    ans=runin(a)
    sho="Case #"+str(i)+": "+str(ans)
    print sho
    out.append(sho)


r = open("C:\Users\SJ\Downloads\C2.out","w")
for i in out:
    r.write(i+"\n")





            
            
                    
                
        
                
                
            
            
        
        

        
        
        
