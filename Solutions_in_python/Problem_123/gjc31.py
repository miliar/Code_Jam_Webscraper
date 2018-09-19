def steps(a,b):
    steps=0
    if (a == 1): return 9999999999999999,9999999999999999
    while (a<=b):
        a += (a-1)
        steps+=1
        #print a,
    return steps, a

f = open("1.txt","r")

T = int(f.readline())
for case in range(1,T+1):
    print "Case #" + str(case)+":",
    A, N = map(int, f.readline().split(" "))
    motes = map(int, f.readline().split(" "))
    motes.sort()
    #print "motes : ",
    #print motes
    #print "Intial A: ",
    #print A
    operation=0
    pos=0
    for e in motes:
        #print "e:",
        #print e,
        #print " A : " +str(A),
        if A>e:
            A+=e
        else:
            addVal= A-1
            if (A + addVal) > e:
                #add
                A+=addVal
                A+=e
                operation+=1
            else:
                #remove
                stps, newA = steps(A, e)
                #print "stps : " + str(stps),
                if stps >= (len(motes)-pos):
                    operation+=(len(motes)-pos)
                    break
                else:
                    A=newA
                    A+=e
                    operation+=stps
            
        pos+=1
        #print " A : " +str(A),
        #print " operation : "+str(operation)
    print operation
    #raw_input()
