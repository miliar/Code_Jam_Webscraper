def x_o_wins(a,b,c,d) :
   
    for e in range(0,4):
        
        
        if (a[e]=='X' or a[e]=='T') and (b[e]=='X' or b[e]=='T') and (c[e]=='X' or c[e]=='T') and (d[e]=='X' or d[e]=='T'):
            return 1
                 
        if (a[e]=='O' or a[e]=='T') and (b[e]=='O' or b[e]=='T') and (c[e]=='O' or c[e]=='T') and (d[e]=='O' or d[e]=='T'):            
            return 2
    if (a[0]=='X' or a[0]=='T') and (b[1]=='X' or b[1]=='T') and (c[2]=='X' or c[2]=='T') and (d[3]=='X' or d[3]=='T'):
        return 1
    
    if (a[0]=='O' or a[0]=='T') and (b[1]=='O' or b[1]=='T') and (c[2]=='O' or c[2]=='T') and (d[3]=='O' or d[3]=='T'):        
        return 2
    
    if (d[0]=='X' or d[0]=='T') and (c[1]=='X' or c[1]=='T') and (b[2]=='X' or b[2]=='T') and (a[3]=='X' or a[3]=='T'):
        return 1
    if (d[0]=='O' or d[0]=='T') and (c[1]=='O' or c[1]=='T') and (b[2]=='O' or b[2]=='T') and (a[3]=='O' or a[3]=='T'):         
        return 2

    comb=a+b+c+d
    
    i=1
    c=1
    while c<5:
        comb1=comb[(i-1):c*4]
        
        if (comb1[0]=='X' or comb1[0]=='T') and (comb1[1]=='X' or comb1[1]=='T') and (comb1[2]=='X' or comb1[2]=='T') and (comb1[3]=='X' or comb1[3]=='T'):            
            return 1
        if (comb1[0]=='O' or comb1[0]=='T') and (comb1[1]=='O' or comb1[1]=='T') and (comb1[2]=='O' or comb1[2]=='T') and (comb1[3]=='O' or comb1[3]=='T'):            
            return 2
        i=i+4
        c=c+1
    return 0

def not_comp_chk(a,b,c,d):
     for e in range(0,4):
        if a[e]=="." or b[e]=="." or c[e]=="." or d[e]==".":
            return 3
     return 0




        
file=open("c:/users/rhv/Desktop/code_jam/A-large.in","r")
file1=open("c:/users/rhv/Desktop/code_jam/out_large.txt","w")
i=0
m=file.readline()
l=m.split()

while i<int(l[0]):
    a=file.readline()
    b=file.readline()
    c=file.readline()
    d=file.readline()
    e=file.readline()
    a1=str(a.split())
    b1=str(b.split())
    c1=str(c.split())
    d1=str(d.split())
    a1=a1[2:6]
    b1=b1[2:6]
    c1=c1[2:6]
    d1=d1[2:6]
    result=x_o_wins(a1,b1,c1,d1)
    
    if result==0:
        
        result=not_comp_chk(a1,b1,c1,d1)
    if result==0:
        ans = "Draw"
    if result==1:
        ans="X won"
    if result==2:
        ans="O won"
    if result==3:
        ans="Game has not completed"
    a = "Case #" + str(i+1) +": "+str(ans)+"\n"
    file1.write(a)
    i=i+1
file.close()
file1.close()
    

        
    

            
        
    

    
        
  
 
    
