import copy
f = open('/home/rakesh/Desktop/codeJam/B-small-attempt1.in', 'r')
fout = open('/home/rakesh/Desktop/codeJam/output8.in', 'w')
tempCounter=1
testCaseCounter=1
for line in f:
    if(tempCounter%2==0 or tempCounter==1):
        tempCounter+=1
        continue
    tempCounter+=1
    line.rstrip()
    strarry=line.split()
    array=map(int, strarry)
    maxFact=max(array)
    array=sorted(array)
    minitime=max(array)
    #print array
    import time
    def getTotalTime(factVal):
        temparray=copy.deepcopy(array)
        time1=0
        counter=0
        
        while(max(temparray)>factVal and counter<len(temparray)):
            if(time1>minitime):
                return time1+factVal
                
            if(temparray[counter]<=factVal):
                counter+=1
                continue
            splitval1=factVal
            splitval2=temparray[counter]-factVal
            temparray.pop(counter)
            temparray.insert(0,splitval1)
            temparray.insert(0,splitval2)
            
            temparray=sorted(temparray)
            counter+=1
            time1+=1
        
        return time1+factVal
            
        
    
    #print maxFact
    
    for i in range(1,maxFact):
        #print "i is",i
        tempTime=getTotalTime(i)
        #print "tempTime is",tempTime
        if(tempTime<minitime):
            minitime=tempTime
            
            
    #print "miniTime is ",minitime
    outputstr="Case #%d: %d\n"%(testCaseCounter,minitime)
    testCaseCounter+=1
    #print outputstr
    fout.write(outputstr)

    
    

    

    