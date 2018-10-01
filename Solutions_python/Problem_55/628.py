import sys

def showMeTheMoney(p,r,n,k,cgin):
    ret="Case #"
    i=1
    money=0
    cg=cgin
    
    while(i<=r):
        
        acum=0
        entran=[]
        index=0
        while(index<len(cg)):
           
            if (acum + int(cg[index])) > k:
                
                break
            else:
                entran.append(cg[index])
                acum+=int(cg[index])
                money+=int(cg[index])
            index+=1
        cg=cg[index:len(cg)]+entran
        
        i+=1
        


    return ret+str(p)+": "+str(money)
    

def runRC():
    print sys.argv
    fin=open(sys.argv[1],'r')
    fout=open("res.out", "w")
    num=int(fin.readline())
    p=1
    while(p<=num):
        
        datos=fin.readline()
        groups=fin.readline()
        cdat= datos.split(" ")
        cg=groups.split(" ")
        r=int(cdat[0])
        k=int(cdat[1])
        n=int(cdat[2])
        fout.write(showMeTheMoney(p, r,n, k, cg)+ "\n")
        p+=1
        

runRC()
