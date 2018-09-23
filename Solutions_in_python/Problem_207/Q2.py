def Ans(colors):
    for i in range(len(colors)): colorLine[i]=int(colors[i])
    N=0
    for x in colors: N+=x
    #For each O,G,and Violet, remove 1 of the complementary colour - V must be flanked like : BVB, which looks like B
    
    #We need one more of the flankers than the others
    if(colors[3]>colors[0]): return "IMPOSSIBLE"
    elif(colors[3]==colors[0]):
        #There can't be any flanking, so everyone else must be zero, or we're both 0
        if(colors[3] is not 0):
            if(N-colors[3]*2 is not 0): return "IMPOSSIBLE"
            else: #Return an alternating string of the two
                l=[]
                for i in range(colors[3]):
                    l.append('G')
                    l.append('R')
                return "".join(l)
                
    else: colors[0]-=colors[3]

    
    if(colors[5]>colors[2]): return "IMPOSSIBLE"
    elif(colors[5]==colors[2]):
        if(colors[5] is not 0):
            if(N-colors[5]*2 is not 0): return "IMPOSSIBLE"
            else:
                l=[]
                for i in range(colors[5]):
                    l.append('V')
                    l.append('Y')
                return "".join(l)
                
    else: colors[2]-=colors[5]

    
    if(colors[1]>colors[4]): return "IMPOSSIBLE"
    elif(colors[1]==colors[4]):
        if(colors[1] is not 0):
            if(N-colors[1]*2 is not 0): return "IMPOSSIBLE"
            else:
                l=[]
                for i in range(colors[3]):
                    l.append('O')
                    l.append('B')
                return "".join(l)
                
    else: colors[4]-=colors[1]

    #Now, if any one color has more than half, we can't do it
    sum=colors[0]+colors[2]+colors[4]
    if(colors[0]*2 > sum): return "IMPOSSIBLE"
    if(colors[2]*2 > sum): return "IMPOSSIBLE"
    if(colors[4]*2 > sum): return "IMPOSSIBLE"

    #Otherwise we can do it - place them in the obvious way
    ring=[]
    if(colors[0]>0):
        ring.append(0)
        colors[0]-=1
    elif(colors[2]>0):
        ring.append(2)
        colors[2]-=1
    elif(colors[4]>0): #N>=3 so one of these must fire
        ring.append(4)
        colors[4]-=1
    
    for i in range(sum-1): #We've lost one from the original append - just stick stuff on - where you have a choice, use the abundant one
        if(i==sum-2): #Worry about the first one
            options=[0,2,4]
            options.remove(ring[-1])
            if(ring[0] is not ring[-1]): options.remove(ring[0])                        

            for x in options:
                if(colors[x]>0):
                    ring.append(x)
                    colors[x]-=1
                    break
                            
        else:
            if(ring[-1]==0): #Choose the larger of the avaliables
                if(colors[2]>colors[4]):
                        ring.append(2)
                        colors[2]-=1
                else:
                        ring.append(4)
                        colors[4]-=1

            elif(ring[-1]==2): 
                if(colors[0]>colors[4]):
                        ring.append(0)
                        colors[0]-=1
                else:
                        ring.append(4)
                        colors[4]-=1

            elif(ring[-1]==4): 
                if(colors[2]>colors[0]):
                        ring.append(2)
                        colors[2]-=1
                else:
                        ring.append(0)
                        colors[0]-=1

    #So now we have a bunch of indexes - now to turn them into characters
    chars=['R','O','Y','G','B','V']
    charRing=[]
    for x in ring:
        if(x==0): #Fill in the complements
            if(colors[3]>0):
                colors[3]-=1
                charRing.append(chars[0])
                charRing.append(chars[3])
                charRing.append(chars[0])
            else: charRing.append(chars[0])
                
        if(x==2): #Fill in the complements
            if(colors[5]>0):
                colors[5]-=1
                charRing.append(chars[2])
                charRing.append(chars[5])
                charRing.append(chars[2])
            else: charRing.append(chars[2])

        if(x==4): #Fill in the complements
            if(colors[1]>0):
                colors[1]-=1
                charRing.append(chars[4])
                charRing.append(chars[1])
                charRing.append(chars[4])
            else: charRing.append(chars[4])
        
        
    return "".join(charRing)


numCases=int(raw_input())
for case in range(numCases):
    colorLine=raw_input().split(" ")[1:] #ROYGBV - ignore N
    
    print("Case #"+str(case+1)+": "+Ans(colorLine))
    
