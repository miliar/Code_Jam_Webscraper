inputValue=int(input())
inputList=[None]*inputValue
for i in range(inputValue):
    input1=input()
    myarr=list(str(input1))
    for j in range(len(myarr)-1,0,-1):
        if(int(myarr[j-1])>int(myarr[j])):
            myarr[j-1]=""+str(int(myarr[j-1])-1)
            for k in range(j,len(myarr)):
                myarr[k]='9';
        else:    
            continue
    myarr1="".join(myarr);
    inputList[i]=int(myarr1)  ;  
for n in range(len(inputList)):
    output="Case #"+str((n+1))
    output=str(output)+": "+str(inputList[n])
    print(output)