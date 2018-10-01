#!/usr/bin/python3
#encoding=UTF-8
def readCase(dir):
    f=open(dir,'r')
    caseMatrix=[]
    while True:
        line=f.readline()
        if line:
            caseMatrix.append(line.strip())
        else:
            break
    f.close()
    return caseMatrix[1:]
def divisionNum(Num):
    flag=False
    pre=10
    restlist=[]
    while Num>10:
        tmp=Num%10
        restlist.append(tmp)
        Num=Num/10
    restlist.append(Num)
    for i in range(0,len(restlist)-1):
        if restlist[i]<restlist[i+1]:
            flag=True
            break
    return flag

def findTidyNumber(N):
    #print(N)
    if N<10:
        return N
    else:
        while N>10:
            if divisionNum(N):
                #print('debug2')
                return findTidyNumber(N-1)
            else:
                return N
        
     

if __name__=='__main__':
    answer=[]
    cases=readCase('/home/ghh/workSpace/B-large.in')
    
    #print(cases)
    
    for i in range(0,len(cases)) :
        case=cases[i]
        line=[]
        if len(case)==1:
            line.append(case[0])
        if len(case)>1:
                for j in range(1,len(case)):
                    if case[j-1]<=case[j]:
                        line.append(case[j-1])
                        if j==len(case)-1:
                            line.append(case[j])
                    else:
                        temint=int(case[j-1])-1
                        line.append(str(temint))
                        for l in range(j,len(case)):
                            line.append('9')
                        #line[j-1]=str(int(line[j-1])-1)
                        k=j-1
                        while k>=1:
                            if line[k]<='0':
                                line[k]='9'
                                line[k-1]=str(int(line[k-1])-1)
                            if line[k]<line[k-1]:
                                line[k-1]=str(int(line[k-1])-1)
                                line[k]='9'
                            k-=1
                        break
        tmp='Case #'+str(i+1)+': '
        for m in range(0,len(line)):
            if line[m]=='0':
                m+=1
            else:
                break
        for n in range(m,len(line)):
            tmp+=line[n]
        tmp+='\n'
        answer.append(tmp)
    for i in range(0,len(case)):
        if line[i] =='0':
            i+=1
        else:
            break
    
    for i in answer:
        print(i)
    

            
        