def row_chk(row,col,*ele):
    if row==1 or col==1:
        return 1
    for i in range(0,row):
        for j in range(0,col):
            flag = 0
            flag1=0
            for k in range(0,row):
                if ele[i][j]<ele[k][j]:
                    flag=1
                    break
            if flag==1:
                for l in range(0,col):
                    if ele[i][j]<ele[i][l]:
                        flag1=1
                        break
            if flag1==1:
                return 0
    return 1


            
file=open("c:/users/rhv/Desktop/code_jam/b.txt.in","r")
file1=open("c:/users/rhv/Desktop/code_jam/out.txt","w")
i=0
m=file.readline()
l=m.split()

while i<int(l[0]):
    a=file.readline()
    a1=a.split()
    row=int(a1[0])
    col=int(a1[1])
    ele=[]
    for j in range(0,row):
        m=file.readline()
        ele.append(m.split())
    ret=row_chk(row,col,*ele)
    if ret==1:
        ans="YES"
    else:
        ans="NO"
    a = "Case #" + str(i+1) +": "+str(ans)+"\n"
    file1.write(a)
    i=i+1
    
file.close()
file1.close()
    

        
        
        
    
    

                
                        
