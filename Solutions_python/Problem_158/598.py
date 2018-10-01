InFile = open('D-small-attempt0.in','r')
OutFile = open('Output.out','w')

T = int(InFile.readline().rstrip('\n'))

for i in range(T):

    line = [int(x) for x in InFile.readline().rstrip('\n').split(' ')]
    X = int(line[0])
    R = int(line[1])
    C = int(line[2])

    N = min(R,C)
    M = max(R,C)

    if   X == 1:
        OutFile.write('Case #'+str(i+1)+': GABRIEL\n')
        
    elif X == 2:
        if (N*M)%2 != 0:
            OutFile.write('Case #'+str(i+1)+': RICHARD\n')
        else:
            OutFile.write('Case #'+str(i+1)+': GABRIEL\n')
                          
    elif X == 3:
        if (N*M)%3 != 0:
            OutFile.write('Case #'+str(i+1)+': RICHARD\n')
        elif  N == 1:
            OutFile.write('Case #'+str(i+1)+': RICHARD\n')              
        else:
            OutFile.write('Case #'+str(i+1)+': GABRIEL\n')                          
               
    elif X == 4:
        if (N*M)%4 != 0:
            OutFile.write('Case #'+str(i+1)+': RICHARD\n')
        elif  ((N == 1)or(N == 2)):
            OutFile.write('Case #'+str(i+1)+': RICHARD\n')              
        else:
            OutFile.write('Case #'+str(i+1)+': GABRIEL\n')      
        

    #OutFile.write('Case #'+str(i+1)+': GABRIEL\n')
    #OutFile.write('Case #'+str(i+1)+": RICHARD\n')
        

InFile.close()
OutFile.close()
