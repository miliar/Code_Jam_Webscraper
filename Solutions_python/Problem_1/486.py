filename="A-large.in"
inputfile=open(filename)
outputfile=open(filename+".out","w")
N=int(inputfile.readline())
for X in range(N):
    S=int(inputfile.readline())
    se=[]
    for s in range(S):
        se.append(inputfile.readline().rstrip())
    Q=int(inputfile.readline())
    query=[]
    for q in range(Q):
        query.append(inputfile.readline().rstrip())
    Y=0
    testSet=set()
    for s in query:
##        outputfile.write(s+"\n")
        testSet.add(s)
##        outputfile.write(str(testSet)+"\n")
        if len(testSet)==S:
            Y=Y+1
            testSet=set()
            testSet.add(s)
    outputfile.write("Case #"+str(X+1)+": "+str(Y))
##    outputfile.write("\n")
##    outputfile.write(str(se))
##    outputfile.write("\n")
##    outputfile.write(str(query))
##    outputfile.write("\n")
    outputfile.write("\n")
inputfile.close()
outputfile.close()
