fi=open("A-large.in",'r')
fo=open("A-large.out",'w')

t=int(fi.readline().strip())
for case in range(t):
    fo.write("Case #"+str(case+1)+":\n")
    line=fi.readline().strip().split()
    r=int(line[0])
    c=int(line[1])
    pic=[]
    
    check=True
    
    for ro in range(r):
        l=fi.readline().strip()
        line=[]
        for char in l:
            line.append(char)
        pic.append(line)
    pic.append(['.']*c)
    
    for ro in range(0,r):
        
        cur=pic[ro]
        nex=pic[ro+1]
        co=0
        
        while co<len(cur):
            if cur[co]=='#':
                
                if co==c-1:
                    check=False
                    break
                elif cur[co+1]=='#':
                    if nex[co]=='#' and nex[co+1]=='#':
                        pic[ro][co]='/'
                        
                        pic[ro][co+1]='\\'
                        pic[ro+1][co]='\\'
                        pic[ro+1][co+1]='/'
                        co+=2
                    else:
                        
                        check=False
                        break
                    
                else:
                    check=False
                    break
            else:
                
                co+=1
        if check==False:
            break
      
    if check==False:
        fo.write("Impossible\n")
    else:
        for ro in range(r):
            for co in range(len(pic[ro])):
                fo.write(pic[ro][co])
            fo.write("\n")
            
            
    
    
fi.close()
fo.close()
            