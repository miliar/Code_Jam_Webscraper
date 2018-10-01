def standingOvationNeeded(filename):
    """
    GCJ: (A) Standing Ovation Needed
    """
    # ## Input how many cases
    
    f = open(filename, 'r')    
    T = int(f.readline().strip())
    if T<1 or T>100:
        exit("1, T Limits exceeded.")
        
    tn = []  
        
    # ## Input Test Cases
    for i in range(T):
        tn.append(f.readline().strip())
    f.close()        
    for i in range(T):
        tn[i] = tn[i].strip().split(' ')
        smax = int(tn[i][0])
        si = tn[i][1]        
        ppl = 0
        invite = 0
        for j in range(smax+1):
            if j>ppl and (j-ppl)>invite:
                invite = j-ppl
            ppl += int(si[j])
            
        # OUTPUT Write
        g = open(filename.strip(".in")+"-Ouput.out", 'a')
        g.write("Case #"+str(i+1)+": "+str(invite)+'\n')
    g.close()

# ################################################# #


if __name__=="__main__":
    
    filename = "A-large.in"
    standingOvationNeeded(filename)