import sys


def winp(flist,num):
        win=float(0)
        i=-1
        tot=float(0)
        for c in flist:
            i += 1
            if i == num:
                continue
            if c=='1':
                win += 1
            if c!='.':
                tot += 1
        
        return win/tot
        


file = open(sys.argv[1],'r');

testcase = int(file.readline().strip())


for iii in range(1,testcase+1):
     
    num = int(file.readline().strip())
    
    winlist=[]
    wpl=[]
    owpl=[]
    oowpl=[]
    
    for i in range(0,num):
        games = file.readline().strip()
        gamesl = list(games)
        winlist.append(gamesl)
        
        

    for i in range(0,num):
        wpl.append(winp(winlist[i],-2))
        
    for k in range(0,num):
        owp = float(0)
        tot = float(0)
        for j in range(0,num):
               if k == j:
                   continue
               if winlist[k][j] != '.':
                   tot += 1
                   owp+= winp(winlist[j],k)
        owpl.append (owp / tot)
           
    for j in range(0,num):
        oowp = float(0)
        tot = float(0)
        for k in range(0,num):
               if j == k :
                   continue
               if winlist[k][j] != '.':
                   tot += 1
                   oowp += owpl[k]
        oowpl.append(oowp/tot)

    print "Case #"+str(iii)+":"
    for i in range(0,num):
        print str(0.25 * wpl[i] + 0.50 * owpl[i] + 0.25 * oowpl[i])
    

       
   

            
        
        
        
