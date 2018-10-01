def findCommon(lst1,lst2):
    t=[]
    for i in lst1:
        if(i in lst2):
            t.append(i)
    
    return t


f=open("A-small-attempt1.in","r")
f1=open("output.txt","w")

lst=[]
t=[]
c=0
T=0
ans=[]
for line in f:
    if(c==0):
        T=line.replace("\n","")
        T=(int)(T[0:len(T)])
        c+=1
    elif(c%5==1):
        ans.append(line.replace("\n",""))
        c+=1
    elif(c!=0 & c%5==0 ):
        t.append(line.replace("\n","").split(" "))
        c+=1
    if(len(t)==4):
        lst.append(t)
        t=[]

ans1=0
ans2=0
c=0
case=0
for j in range(0,T):
   
   i=lst[c]
   ii=lst[c+1]

   ans1=(int)(ans[c])-1
   ans2=(int)(ans[c+1])-1
   c+=2

   s="Case #"+str(j+1)+": "
   x=findCommon(i[ans1],ii[ans2])
   if(len(x)==1):
       print  x[0]
       s+=str(x[0])+"\n"

   elif(len(x)>0):
        print "Bad magician!"
        s+="Bad magician!"+"\n"
   else:
        print "Volunteer cheated!"
        s+="Volunteer cheated!"+"\n"

   f1.write(s)

f.close()
f1.close()


        
    
