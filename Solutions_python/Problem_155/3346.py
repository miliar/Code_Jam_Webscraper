
with open ("google_input.txt","r+") as f:
    
    case = int(f.readline())
    sw = case
    w = open("output_large.txt","a")
    c = 1
    while(case != 0):
        
        total = 0
        friend = 0
        i = 0
        temp = f.readline()
        x = temp.split()
        smax = int(x[0])
        p = int(x[1])
        power = smax
        for j in range (0,sw+1):
            for i in range (0,smax+2):
                var = p/(10**(power))
            
            #print var
                if (i>total)and(var>0):
                    friend = friend + (i-total)
                    
                    total = total+(i-total)
            
                total = total + var
            
                if var>0:  
                    p = p - (10**(power)*var)
                if(power>=0):
                    power = power-1
        #print c,friend
        string = "Case #%d: %d"%(c,friend)
        w.write(string+"\n")
        #print(smax,p)
        #print friend

        c = c+1
        case = case -1
        
        
    w.close()
    f.close()
    
