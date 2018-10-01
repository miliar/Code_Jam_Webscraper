InFile = open('A-large.in','r')
OutFile = open('Output.out','w')

T = int(InFile.readline().rstrip('\n'))

for i in range(T):

    N = int(InFile.readline().rstrip('\n'))
    line = [int(x) for x in InFile.readline().rstrip('\n').split(' ')]

    minNum = 0
    maxDif = 0
    minNumCont = 0
    for j in range(N-1):
        if line[j]>line[j+1]:
            minNum += line[j]-line[j+1]
            maxDif = max(maxDif,line[j]-line[j+1])

    for j in range(N-1):
        if line[j]>maxDif:
            minNumCont += maxDif
        else:
            minNumCont += line[j]
            

    

    OutFile.write('Case #'+str(i+1)+": "+str(minNum)+' '+str(minNumCont)+'\n')
        

InFile.close()
OutFile.close()
