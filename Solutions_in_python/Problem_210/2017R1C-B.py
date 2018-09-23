file = open("c:/CodeJam/2017/R1/B-large.in")
line = file.readline()

## Number of Test Cases:  1<=T<=100
T=int(line)

## Tests each case
for testcase in range(T):
    # C= # Cameraon Activities
    # J= # Jamie Activities
    [C,J] = map(int,file.readline().split())

    activities=[]
    TotalC=0
    TotalJ=0
    
    for i in range(C):
        [Cstart,Cstop]=map(int,file.readline().split())
        
        activities.append(['C',Cstart, Cstop, Cstop-Cstart])
        TotalC+= Cstop-Cstart

    for j in range(J):
        [Jstart,Jstop]=map(int,file.readline().split())

        activities.append(['J',Jstart,Jstop,Jstop-Jstart])
        TotalJ+= Jstop-Jstart
                                                        


    activities.sort(key=lambda x: x[1])

    sortedactivities=list(activities)

    numberofswitches=0
    numberadjacentactivities=0

    Cgaps=[]
    Jgaps=[]

    for i in range(len(activities)):
        if activities[i][0]==activities[i-1][0]:
            numberofswitches+=2
            if activities[i][0]=='J':
                Jgaps.append([i,(activities[i][1]-activities[i-1][2])%1440])
            elif activities[i][0]=='C':
                Cgaps.append([i,(activities[i][1]-activities[i-1][2])%1440])
        else:
            numberofswitches+=1

    Jgaps.sort(key=lambda x: x[1])
    
    Cgaps.sort(key=lambda x: x[1])

    Jmerges=0
    Cmerges=0
    
    for each in Jgaps:
               
        if TotalJ+each[1]>720:
            break
        else:
            Jmerges+=1
            TotalJ+=each[1]
            numberofswitches-=2

    for each in Cgaps:
        if TotalC+each[1]>720:
            break
        else:
            Cmerges+=1
            TotalC+=each[1]
            numberofswitches-=2   
    
      
        

    print('Case #{}: {}'.format(testcase+1,numberofswitches))
           
file.close() 
        
        
    

    
    

