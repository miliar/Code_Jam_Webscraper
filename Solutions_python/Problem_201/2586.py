# -*- coding: utf-8 -*-


import sys


def getRS(l,x):
    num=0
    for i in range(x+1,len(l)):
        
        if l[i]!=0:
            
            break
        num+=1
        
    return num

def getLS(l,x):
    num=0
    for i in range(x-1,-1  ,-1):
        
        if l[i]!=0:
            
            break
        num+=1
    return num    


    
    

def getNumber(line):
    N,K=line.split()
    listAll = [0]*int(N)
    
    
    
    
    
    
    for d in range(int(K)):
        pos=0
        theLS=0
        theRS=0
        listMin=[-1]*int(N)
        listMax=[-1]*int(N)
        
        
        for idx,val in enumerate(listAll):
            if(listAll[idx]!=0):
                continue                
            theLS=getLS(listAll,idx)
            theRS=getRS(listAll,idx)
            listMin[idx]=min(theLS,theRS)
            listMax[idx]=max(theLS,theRS)
        
        themax1=max(listMin)
        dic1={}
        for i,m in enumerate(listMin):
            
            if(m==themax1):
                dic1[i]=m
                pos=i
        
        if len(dic1)>1:
            mi=-1
            pos=len(listAll)
            
            
            for k in dic1.keys():               
                
                if listMax[k] > mi:
                    mi=listMax[k]
                    
                    pos =k
                    
            
            
    
            
        #print(pos)    
        #print(pos,listMin,listMax)
        listAll[pos]=1
        
        
    
    return "{} {}".format(listMax[pos],listMin[pos])

out=open(sys.argv[1]+"_result","w+")
result =[]
with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
num_cases=int(lines[0])

for i in range(1,len(lines)):
    temp= "Case #" + str(i)+ ": " + str( getNumber(lines[i]))
    
    #print(temp)
    result.append(temp)     
out.write("\n".join(result))
out.close()