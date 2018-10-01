T=0
N=0

def botTrust(buttons,case):

    minPath=0
    OPos=1
    BPos=1

    OAcu=0
    BAcu=0
    
    for b in buttons:
        rec=0
        if b[0]=='O':
        
            if int(b[1])>OPos: 
                rec= int(b[1])-OPos-OAcu
            else:
                 rec= OPos-int(b[1])-OAcu 
                        
            if rec > 0:
                minPath+=rec
            else:
                rec=0
            minPath+=1
            OPos=int(b[1])
            BAcu+=rec+1
            OAcu=0

        else:
            if int(b[1])>BPos: 
                rec= int(b[1])-(BPos+BAcu)
            else:
                 rec= (BPos-BAcu)-int(b[1]) 
                      
            if rec > 0:
                minPath+=rec
            else:
                rec=0
            minPath+=1
            BPos=int(b[1])
            OAcu+=rec+1
            BAcu=0  
     
    with open("BotTrust.out",'a') as out:
        out.write("Case #"+str(case)+": "+str(minPath)+"\n")
        case+=1





with open("BotTrust.in") as file:
    T = file.readline()
    case=0
    for line in file.readlines():
        case+=1
        b = line.split()
        N = b[0]
        buttons=[]
        for i in range(1,int(N)+1):
            buttons.append((b[i*2-1],b[i*2]))
        botTrust(buttons,case)


    
            
