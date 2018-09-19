opener=open("A-small-attempt3.in", "r")
Input=opener.read().splitlines()
result=open("out.txt", "w")
cases=int(Input[0])
count=0
invite=0
letter=0
case=0
r=""
for d in Input[1:len(Input)]:
       case+=1
       c=d[2:int(d[0])+3]
       
        
       for k in range(len(c)):
              o=c[letter]
              letter+=1
              if int(o)!=0:
                     if k<=count:
                            count+=int(o)            
            
            
            
                     else:
                            invite+=k
                     
                                                      
                     
                            invite-=count
                            count+=int(o)
                            count+=invite                              
                            
       r+="Case #"+str(case)+": "+str(invite)
       r+="\n"
       
       
       invite=0
       count=0
       letter=0
result.write(r)
result.close()

                