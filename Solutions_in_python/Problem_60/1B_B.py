'''
Google Code Jam 2010
Created by : KenKen
Created on : 2010/05/23
'''

inputfile = open('B-large.in', 'r')
outputfile = open('output.txt', 'w')

C = inputfile.readline().replace("\n", "")   # Read the first line
C = int(C)

caseNo = 0
while caseNo < C:
    caseline1 = inputfile.readline().replace("\n", "")
    if not caseline1:
        break
     
    (N,K,B,T) = map(int, caseline1.split(" "))
    
    i = 0
    caseline2 = inputfile.readline().replace("\n", "")
    X = map(int, caseline2.split(" "))
    caseline3 = inputfile.readline().replace("\n", "")
    V = map(int, caseline3.split(" "))
    
    #for i in range(0, N):
    Xt = map(lambda x:x*T, V)
    Xt = map(lambda x:x[0]+x[1], zip(Xt, X))
    
    if len(filter(lambda x:x>=B, Xt)) < K:
        swapNo = "IMPOSSIBLE"
    else:
        swapNo = 0
        reached = 0
        while reached < K:
            if Xt[-1] >= B:
                reached += 1
                Xt.pop()
            else:
                p = 0
                while Xt[-1-p] < B:
                    p += 1
                reached += 1
                Xt.pop(-1-p)
                swapNo += p
        
    print >> outputfile, "Case #%d: %s" % (caseNo+1, swapNo)
    caseNo += 1
inputfile.close()
outputfile.close()
