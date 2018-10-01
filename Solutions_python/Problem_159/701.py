cases=int(input())
out_1=[];out_2=[]
for i in range (0,cases):
    num=int(input())
    line=str(input())
    line=line.split()
    line=list(map(int,line))#for convert string list to int list
    prv=line[0];count_1=0;count_2=0;rata_found=False;maxdef=0
    for j in range(1,len(line)):
        if prv > line[j]:
            sub=prv-line[j]
            if sub>maxdef:
                maxdef=sub
            count_1+=(sub)
        prv=line[j]
    
        
   
    pr=line[0]
    for k in range(1,len(line)):
        if pr<maxdef:
            count_2+=pr
        else:
            count_2+=maxdef
        pr=line[k]    
    out_1.append(count_1)
    out_2.append(count_2)
            
            
        
    








out_1.reverse()
out_2.reverse()
lenprint=0
while len(out_1):
    lenprint+=1
    print("Case #",end="")
    print(lenprint,end="")
    print(": ",end="")
    print(out_1.pop(),end=" ")
    print(out_2.pop())
    
