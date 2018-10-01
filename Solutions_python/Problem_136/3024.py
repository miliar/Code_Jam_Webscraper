f = open('B-large.in', 'r')
#f = open('B.txt', 'r')
testcases = f.readline()
testcases = int(testcases)

f2 = open('B-output.txt','w')


for x in range(1, testcases+1):
    r = 2.0
    time = 0
   
    R = r
    
    line = f.readline()
    line = [float(k) for k in line.split(' ')]
    C = line[0]
    F = line[1]
    X = line[2]
    #print "C=%f, F=%f, X=%f" % (C,F,X)
    wait = X/R
    oldtime = wait
        
    buy = C/R
    newtime = buy
    
    i = 1
    time = time+buy
    
    oldest = oldtime
    
    while newtime < oldtime:
       
        #print "newtime=%f, oldtime=%f,time=%f" % (newtime,oldtime,time)
        R  =R+F
        wait = X/R
        buy = C/R
        oldtime = time + wait
     
        R = R +F
        wait = X/R
        newtime = time + buy + wait
        
        if oldtime > oldest:
            newtime = oldtime + 10
            oldtime = oldest
        #print "buy=%f, wait=%f" % (buy,wait)
        #print "newtime=%f, oldtime=%f, R=%d" % (newtime,oldtime,R)
        time = newtime - wait
        #print "time=%f\n" % time
        R=R-F
        
        
    if x == testcases:    
        #print "Case #%d: %.7f" % (x,oldtime)
        f2.write("Case #%d: %.7f" % (x,oldtime));
        
    if x<testcases:
        #print "Case #%d: %.7f\n" % (x,oldtime)
        f2.write("Case #%d: %.7f\n" % (x,oldtime));
        
    
f2.close()
f.close()